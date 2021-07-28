from urllib import request

#requesting from server
with request.urlopen("http://eng.pdn.ac.lk") as response:
    body = response.read()

    #part a- getting the response code
    response_code = response.getcode()
    print ("Response Code: ",response.getcode())
    
