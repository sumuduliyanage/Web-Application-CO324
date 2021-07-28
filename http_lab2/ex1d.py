from urllib import request

#requesting from server
with request.urlopen("http://eng.pdn.ac.lk") as response:
    body = response.read()

    #part d - type of the body variable
    print ("Type of Body Variable: ",type(body))
    print()
