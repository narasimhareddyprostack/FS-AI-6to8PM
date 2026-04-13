#create
product={
    'id':1,
    'name':'Marker Pen',
    'price':30,
    'colors':['Red','Blue','Yellow']
}

#read
print(product)


#update 
#update product Name
product['name']="New Stylish Marker Pen"
print(product)

#delete
del product['id']
print(product)