import logging
from pprint import pformat
from typing import Sequence, Mapping, Tuple
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
import random, string, logging
import grpc, task_pb2, task_pb2_grpc


def random_string_generator(str_size):
    return "".join(random.choice(string.ascii_letters) for x in range(str_size))


# Test that will be used to grade addTask
def test_add(stub, count) -> Mapping[int, str]:
    tasks = {}
    for i in range(count):
        desc = random_string_generator(99)
        task: task_pb2.Task = stub.addTask(wrappers_pb2.StringValue(value=desc))
        logging.debug(f"Added Task {pformat(task)}")
        tasks[task.id] = task.description

    return tasks


def test_list(stub, tasks: Mapping[int, str]) -> None:
    tasklist: task_pb2.Tasks = stub.listTasks(task_pb2.TaskQuery(selected = ['ASSIGNED','PROGRESSING']))
    for t in tasklist.pending:
        logging.debug(f"Task {pformat(t)}")
        # Is the proper task desc is returned for this id?
        #assert t.description == tasks[t.id]


# Test that will be used to grade delTask
def test_del(stub, tasks: Mapping[int, str]) -> None:
    for id, desc in tasks.items():
        task = stub.delTask(wrappers_pb2.UInt64Value(value=id))
        logging.debug(f"Deleted Task {pformat(task)}")
        assert desc == task.description

def test_edit(stub, tasks: Mapping[int, str]) -> None:
    task1 = stub.editTask(task_pb2.Task(id =5, description = "hi", state = task_pb2.ASSIGNED))
    task2 = stub.editTask(task_pb2.Task(id=3,description='Modified description',state=task_pb2.ASSIGNED))
    task3 = stub.editTask(task_pb2.Task(id=3,description='Modified description', state=task_pb2.PROGRESSING))
    task4 = stub.editTask(task_pb2.Task(id=2,description='Modified description',state=task_pb2.ASSIGNED))
           
    print(task1.description)
    print(task2.description)
    print(task3.description)
    print(task4.description)
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = task_pb2_grpc.TaskapiStub(channel)
        tasks = test_add(stub, 10)
        test_edit(stub,tasks)
        test_list(stub, tasks)
       
       
