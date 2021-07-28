from urllib import request

#requesting from server
with request.urlopen("http://eng.pdn.ac.lk") as response:
    body = response.read()

    #part c - size of the response body
    response_body_size = len(body)
    print ("Response Body Size: ",response_body_size)
