from urllib import request
from urllib import parse

#part l(L)
name = parse.quote("සුමුදු")
with request.urlopen("https://www.duckduckgo.com/?q="+name+"&format=json&pretty=1") as query_l:
    headers_l = query_l.headers.items()
    body_l = query_l.read().decode('utf-8')
    print ("Part L")
    print (body_l)
    print()
