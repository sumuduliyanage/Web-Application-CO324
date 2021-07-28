
def load_users_to_lists(filename):
    #took two lists named ids and logins
    ids, logins = list(), list()

    #opening the file
    with open(filename) as f:

        #reading the file line by line
        for line in f:
            #split by space
            id, login = line.split()
            #adding the newly read id into ids list
            ids.append(id)
            #adding the newly read login into logins list
            logins.append(login)
    #return both lists
    return ids, logins



#bellow , I printed the return values of the load_users_to_lists function
filename = "userdata.txt"
print (load_users_to_lists(filename))

