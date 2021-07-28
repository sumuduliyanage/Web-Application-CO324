def load_users_to_list(filename):
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



filename = "userdata.txt"
ids, logins = load_users_to_list(filename)

#question c- we get a zip object
#those lists are zipped and created a zip object called combined
combined = zip(ids,logins)
print (combined)#printing the zip object
print(tuple(combined))#printing all the tuples in zip object

#part d
combined_reversed = zip(logins,ids)
print (combined_reversed)
print (tuple(combined_reversed))#the tuple values are interchanged
