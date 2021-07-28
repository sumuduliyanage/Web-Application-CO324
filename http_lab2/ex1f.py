from urllib import request

#part f - requesting a non  url-uncomment to see the errors

#comment one and run other...you can't run both 
with request.urlopen("http://eng.pdn.ac.lk/unknown") as unknown_response1:
    print(unknown_response1)

#run next
#with  request.urlopen("http://unknown.pdn.ac.lk") as unknown_response2:
#    print(unknown_response2)
