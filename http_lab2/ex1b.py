from urllib import request

#requesting from server
with request.urlopen("http://eng.pdn.ac.lk") as response:
    body = response.read()

    #part b - os and the server
    response_headers = response.headers.items()
    print (response_headers)
