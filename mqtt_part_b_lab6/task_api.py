
# E/16/200
#Lakmali B. L. S
#CO324
#lab6_part_b 1 and 2 questions are implemented here

import paho.mqtt.client as mqtt
import random
import json
import threading
import sys
import uuid
import time

#all tasks are inserted into this dictionary along with their task id
tasks = {} 


def on_connect(client, userdata, flags, rc):
    print(' Successfully Connected To The Broker','\n')
    print ('_' * 40 , '\n')
        
    # subscribing to the ADD and DELETE topics
    client.subscribe("taskApi/ADDtask1" , qos = 2)
    client.subscribe("taskApi/DELETEtask1" , qos = 2)
    client.subscribe("taskApi/EDITtask1" , qos = 2)
    
    InputThread(clientId, client).start()


def on_message(client, userdata, msg):
    
    payload = json.loads(msg.payload)
    
    # adding a task into task api
    if(msg.topic == "taskApi/ADDtask1"):#checking the topic
        if payload['id'] not in tasks.keys():# add the task of only the recieved task Id is not in the client's dictionary
            tasks[payload['id']] = {'id': payload['id'], 'state':'open', 'description':payload['description']}#add the new task
        

    # deleting a task
    elif(msg.topic == "taskApi/DELETEtask1"):
        if(payload['id'] in tasks.keys()):  # delete the task if the requested Id is in the client's deoctionary
            tasks.pop(payload['id']) #poping from the dictionary
            

    # editing a task
    elif(msg.topic == "taskApi/EDITtask1"):  
        if(payload['id'] in tasks.keys()):

            condition = 0;#this condition will be used later
            
            current = tasks[payload['id']]['state']
            nextone = payload['state']
            #states matching
            if(current== 'open') and (nextone== 'assigned'): 
                condition = 1#if they match, condition is set to one
            elif(current== 'open') and (nextone== 'cancelled'):
                condition = 1
            elif(current== 'assigned') and (nextone== 'progressing'):
                condition = 1
            elif(current== 'progressing' ) and (nextone== 'cancelled'):
                condition = 1
            elif(current== 'progressing') and (nextone== 'done'):
                condition = 1
            else:#otherwise it is zero
                condition = 0
            
            if (condition == 1):#checking condition variable
                tasks[payload['id']] = payload
                
                
   
class InputThread(threading.Thread):
    
    def __init__(self, clientid, client):
        threading.Thread.__init__(self)
        self.clientId = clientid
        self.client = client
     
    
    def run (self):
       while True:
            In = input("Enter the operation(add/delete/edit/list) or 'quit' to exit: ")
            
            # To add a task
            if In == 'add':
                # getting a desscription
                desc = input("Enter the descrption: ")
                # create a UUID for the task with the combination of clientId and the lenght of the task dictionaty
                taskid =  str(uuid.uuid1())
                print("Added task id: ",taskid," ",desc)
                # publish to the ADD topic
                client.publish("taskApi/ADDtask1", json.dumps({'id':taskid, 'state':'null', 'description':desc}),retain = True ,qos = 2)

            # To delete a task
            elif In == 'delete':
                # get the ID
                id = input("Enter the taskId: ")
                # publish to the DELETE topic
                client.publish("taskApi/DELETEtask1", json.dumps({'id':id, 'state':'null', 'description':"null"}) ,retain = True ,qos = 2)
                print ("Deleted Task Id: " , id)

            #To edit a task
            elif In == 'edit':
                 # get the ID
                id = input("Enter the taskId: ")
                 # get the state
                state = input("Enter the state: ")
                # get a description
                desc = input("Enter the description: ")
                client.publish("taskApi/EDITtask1", json.dumps({'id':id, 'state':state, 'description':desc}) ,retain = True , qos = 2)

            #listig all the tasks
            elif In == 'list':
                for key in tasks.keys():
                    print(key,':',tasks[key])

            elif In == 'quit':
                client.disconnect()
                sys.exit(0)
                
                        
           
if __name__ == "__main__":
        
    clientId = '%.5d'%random.randint(0,10000);
    #clientId = '1111'
    
    print("client Id :", clientId)
    client = mqtt.Client(client_id = clientId, clean_session = False)
    
    client.on_connect = on_connect
    client.on_message = on_message
       
    client.connect("mqtt.eclipse.org", 1883, 60)

    client.loop_forever()
    
    
    
