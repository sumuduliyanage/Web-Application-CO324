from urllib import request
from urllib import parse

#part i
with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1") as query_a:
    headers_a = query_a.headers.items()
    body_a = query_a.read().decode('utf-8')
    print ("Part I")
    print (body_a)
    print ()
