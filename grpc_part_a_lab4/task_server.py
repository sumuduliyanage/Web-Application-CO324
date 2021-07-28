#Author : E/16/200
#Subject : CO324

import logging
from concurrent.futures import ThreadPoolExecutor
from grpc import server
import task_pb2, task_pb2_grpc


class TaskapiImpl:
    """'Implementation of the Taskapi service"""

    def __init__(self):
        # TODO: initialise attributes to store our tasks.
        self.tasks = task_pb2.Tasks()
        pass

    def addTask(self, request, context):
        logging.info(f"adding task {request.description}")
        # TODO: implement this!
        id_for_message = len(self.tasks.tasks)#initial is
        
        if(id_for_message == 0):#initial one
            newTask = task_pb2.Task(id=id_for_message, description=request.description)#new Task
        else:#for others
            newid = self.tasks.tasks[id_for_message-1].id + 1
            newTask = task_pb2.Task(id=newid, description=request.description)#new Task
			
		
        self.tasks.tasks.append(newTask)#adding
        print("Added Id: ", newTask.id)#printing the id
        return task_pb2.Id(id=newTask.id)
				

    def delTask(self, request, context):
        logging.info(f"deleting task {request.id}")
        # TODO: implement this!
        id_temp = -1 #initially we take id as -1
        
        for i in range(len(self.tasks.tasks)):
            if(self.tasks.tasks[i].id == request.id):
                id_temp = i
                print("Removed Id: ", self.tasks.tasks[i].id)
                break
            
        if(id_temp != -1):
            deleted_item = self.tasks.tasks[id_temp]#getting the id of the item to be deleted
            self.tasks.tasks.pop(id_temp)#removing the item from the list
            return task_pb2.Task(id=deleted_item.id, description=deleted_item.description)#returning the task deleted
            
        print("Id Was Not Found")#id_temp is stil -1 
        return
        
        

    def listTasks(self, request, context):
        logging.info("returning task list")
        # TODO: implement this!
        return self.tasks


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with ThreadPoolExecutor(max_workers=1) as pool:
        taskserver = server(pool)
        task_pb2_grpc.add_TaskapiServicer_to_server(TaskapiImpl(), taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
