from urllib import request
from json import loads
from typing import List, Dict
import json
import requests

#part b - question 3
def spider_metadata(urls: List[str]) -> List[List]:
    #taking a list
    list_headers = []

    for i in urls:
        h = requests.head(i,data = {'key':'value'}).headers
        list_headers.append(list(h.items()))

    return list_headers


#for part b
list_head = {"http://www.pdn.ac.lk","http://www.yahoo.lk","http://www.google.com"}
print(spider_metadata(list_head))
print()
