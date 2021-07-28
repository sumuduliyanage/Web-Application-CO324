#function for exercise 3
def load_users_to_dict(filename):
    #initializing the dictionary
    users = dict()
    #file object f
    with open(filename) as f:
        #each line of the file is read
        for line in f:
            id, login = line.split()
            #they are added to the hash table
            users[id ]= login

    #that dictionary is returned
    return users


#uncomment following 2 lines to print the dictionary
#filename = "userdata.txt"
#print (load_users_to_dict(filename))

#for part f
def load_users_to_dict_opposite(filename):
    #initializing the dictionary
    users = dict()
    #file object f
    with open(filename) as f:
        #each line of the file is read
        for line in f:
            id, login = line.split()
            #they are added to the hash table
            users[login ]= id

    #that dictionary is returned
    return users

#uncomment following two lines to print the dictionary where login and id is
#interchanged
#filename = "userdata.txt"
#print (load_users_to_dict_opposite(filename))

#function for exercise g
def load_users_to_dict_comma(filename):

    users = dict()

    with open(filename) as f:

        for line in f:
            #split by comma
            id, login = line.strip().split(",")
            users.update({id : login})

            # add details to the users dict


    return users
#uncomment bellow 2 lines to print the output of load_users_to_dict_comma
#function
#filename = "userdata_comma.txt"
#print (load_users_to_dict_comma(filename))




