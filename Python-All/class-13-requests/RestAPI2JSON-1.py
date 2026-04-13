import requests, json 

#invoke Rest API and write products data into new json file
'''
Usage: fetch all products
Rest API URL: https://dummyjson.com/products
Method Type:  GET
Required Feilds: None
Access Type: Public
'''
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
status_code=resp.status_code
print(type(product_data))
print(status_code)

products=product_data['products']