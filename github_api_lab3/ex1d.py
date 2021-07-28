#Author : E/16/200
#Problem 1 Part d

import requests

with requests.Session() as session:
    session.headers['Authorization'] = 'token ed77e01fbdcc9b54a596e7e366eba88c9cdc251f'#giving the authorization
    response = session.get("https://api.github.com/user")#getting data ---token is used for authentication
    
print(response.json())
