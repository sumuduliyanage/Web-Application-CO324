from urllib import request
from urllib import parse

#part j
with request.urlopen("https://www.duckduckgo.com/?q=Rocco%27s+basilisk&format=json&pretty=1") as query_j:
    headers_j = query_j.headers.items()
    body_j = query_j.read().decode('utf-8')
    print ("Part J")
    print (body_j)
    print()
