import requests

resp=requests.get('https://dummyjson.com/products')
products=resp.json()['products']
print(type(products))