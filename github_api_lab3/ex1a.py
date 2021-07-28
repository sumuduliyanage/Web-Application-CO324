#Author : E/16/200
#Problem 1 Part a


import requests

response = requests.get("https://api.github.com")
print(response.json())#printing the json data
print()
print("Status Code")
print(response.status_code)#printing the status code


