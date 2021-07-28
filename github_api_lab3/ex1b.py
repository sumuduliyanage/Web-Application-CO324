#Author : E/16/200
#Problem 1 Part b

import requests

response = requests.get("https://api.github.com/users/sumuduliyanage")
print(response.json())#printing response
print()
print("Status Code")
print(response.status_code)#printing response code

