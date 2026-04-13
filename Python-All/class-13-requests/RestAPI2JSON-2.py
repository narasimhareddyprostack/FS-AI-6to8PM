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
products=product_data['products']
#print(len(products))

fp=open('product.json','w')
json.dump(products,fp)
print("New JSON File Created successfully")


fp.close()