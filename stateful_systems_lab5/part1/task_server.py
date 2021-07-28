#Author : E/16/200
"""TODO:
    * Implement error handling in TaskapiImpl methods
    * Implement saveTasks, loadTasks
    * Implement TaskapiImpl.editTask (ignoring write conflicts)
    * Fix data race in TaskapiImpl.addTask
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import logging
from pprint import pformat
from typing import Mapping, Sequence, Tuple,List, Dict, Optional, Any

from google.protobuf import (
    any_pb2,
    api_pb2,
    duration_pb2,
    empty_pb2,
    field_mask_pb2,
    source_context_pb2,
    struct_pb2,
    timestamp_pb2,
    type_pb2,
    wrappers_pb2,
)
from grpc import server, StatusCode
from threading import Lock, Thread
import grpc
import task_pb2, task_pb2_grpc


class TaskapiImpl:
    
    def __init__(self, taskfile: str, logfile: str):
        self.taskfile = taskfile
        self.task_id = 0
        self.logfile = logfile
        self.mutex = Lock()

    def __enter__(self):
        """Load tasks from self.taskfile"""
        with open(self.taskfile, mode="rb") as t , open(self.logfile, mode="rb") as lg:
            tasklist = task_pb2.Tasks()
            editlog = task_pb2.Tasks()
            tasklist.ParseFromString(t.read())
            editlog.ParseFromString(lg.read())
            logging.info(f"Loaded data from {self.taskfile}")
            logging.info(f"Loaded data from {self.logfile}")
            self.tasks = {}
            self.task_edit_log: Dict = {int: [List]}
            taskid_temp: int
            
            for item in tasklist.pending:
                self.tasks[item.id] = item
                taskid_temp = item.id

            for log in editlog.pending:
                if log.id in self.task_edit_log:
                    self.task_edit_log[log.id].append(log)
                else:
                    self.task_edit_log[log.id] = [log]

            self.task_id = taskid_temp + 1

            
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Save tasks to self.taskfile"""
        with open(self.taskfile, mode="wb") as t, open(self.logfile, mode="wb") as lg:
            tasks = task_pb2.Tasks(pending = self.tasks.values())
            t.write(tasks.SerializeToString())
            logging.info(f"Saved data to {self.taskfile}")
            logtasks = []
            for i in self.task_edit_log.values():
                logtasks = logtasks + i
            logtasks.pop(0)
            tasklog = task_pb2.Tasks(pending=logtasks)
            lg.write(tasklog.SerializeToString())
            logging.info(f"Saved data to {self.logfile}")
            

    def addTask(self, request: wrappers_pb2.StringValue, context) -> task_pb2.Task:
        with self.mutex as l:
            logging.debug(f"addTask parameters {pformat(request)}")
            #getting the text given
            text_given = request.value
            if (len(text_given) >= 1024):#if it is a large string
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details('To long String!')
                return task_pb2.Task()
            t = task_pb2.Task(id=self.task_id, description=request.value)
            self.tasks[self.task_id] = t
            self.task_id += 1
            return t

    def delTask(self, request: wrappers_pb2.UInt64Value, context) -> task_pb2.Task:
        logging.debug(f"delTask parameters {pformat(request)}")
        key = request.value
        if key not in self.tasks:#checking for valid keys
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Not A Valid Key!')
            return task_pb2.Task()
        return self.tasks.pop(request.value)

    def listTasks(self, request: empty_pb2.Empty, context) -> task_pb2.Tasks:
        logging.debug(f"listTasks parameters {pformat(request)}")
        return task_pb2.Tasks(pending=self.tasks.values())

    #edit task implemented in lab 4 part B
    def editTask(self,request: task_pb2.Task,context) -> task_pb2.Task:
        key = request.id #getting the input id
        if key not in self.tasks:#if it is not a valid id
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Not A Valid Key!')
            return task_pb2.Task()
        self.tasks[request.id] = request #otherwise edditng should be done
        t = self.tasks[request.id]
        return t
    
    #implementing edit task with 
    def destructive_editTask (self,request: task_pb2.Task,context) -> task_pb2.Task:
        
        key = request.id #getting the input id
        message = request.description
        
        if key not in self.tasks:#if it is not a valid id
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Not A Valid Key!')
            return task_pb2.Task()

        if (len(message) >= 1024):#if it is a large string
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('To long String!')
            return task_pb2.Task()
        
        self.delTask(wrappers_pb2.UInt64Value(value = key),context)
        t = self.addTask(wrappers_pb2.StringValue(value = message),context)
        return t


    #implementing edit task with the history
    def nondestructive_editTask (self,request: task_pb2.Task,context) -> task_pb2.Task:
        with self.mutex as l:
            key = request.id #getting the input id
            temp = self.tasks[request.id]
        
            if key not in self.tasks:#if it is not a valid id
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details('Not A Valid Key!')
                return task_pb2.Task()

            if (len(request.description) >= 1024):#if it is a large string
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details('To long String!')
                return task_pb2.Task()
        
            if request.id in self.task_edit_log:
                self.task_edit_log[request.id].append(temp)
            else:
                self.task_edit_log[request.id] = [temp]
            
            self.tasks[request.id] = request #otherwise edditng should be done
            t = self.tasks[request.id]
            return t


TASKFILE = "tasklist.protobuf"
HISTORYFILE = "edittasklog.protobuf"
if __name__ == "__main__":
    Path(TASKFILE).touch()
    Path(HISTORYFILE).touch()
    logging.basicConfig(level=logging.DEBUG)

    with ThreadPoolExecutor(max_workers=1) as pool, TaskapiImpl(
        TASKFILE, HISTORYFILE
    ) as taskapiImpl:
        taskserver = server(pool)
        task_pb2_grpc.add_TaskapiServicer_to_server(taskapiImpl, taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
