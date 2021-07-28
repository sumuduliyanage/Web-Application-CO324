#Author : E/16/200
#Problem 1 Part e

import requests

with requests.Session() as session:
    session.headers['Authorization'] = 'token ed77e01fbdcc9b54a596e7e366eba88c9cdc251f'
    url = "https://api.github.com/user/repos"
    response = session.post(url, json = {'name':'test', 'description':'some test repo'})
    
print(response.json())
