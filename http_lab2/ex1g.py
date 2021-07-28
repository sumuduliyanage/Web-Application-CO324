from urllib import request

#part g - request for a url and just print
with request.urlopen("https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D") as  response_1:

    # print body_1-part g
    body_1 = response_1.read()
    print("part g")
    print (type(body_1))
    print (body_1)
    print()
