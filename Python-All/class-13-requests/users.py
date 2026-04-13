import requests

'''
Usage: fetch all users
Rest API URL: https://jsonplaceholder.typicode.com/users
Method Type:  GET
Required Feilds: None
Access Type:   Public
'''

resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
status_code=resp.status_code

print(type(users))
print(status_code)