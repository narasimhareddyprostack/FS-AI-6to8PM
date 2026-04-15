import requests
'''
Usage: Fetch all users
Rest URL:https://jsonplaceholder.typicode.com/users
Method Type: GET
Required Fields:None
Access Type:Public
'''
API_URL='https://jsonplaceholder.typicode.com/employees'
resp=requests.get(API_URL)
users=resp.json()
print(users)
print("GE")