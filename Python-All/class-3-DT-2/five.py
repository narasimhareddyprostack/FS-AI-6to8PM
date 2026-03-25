#create
product={
    'id':1,
    'name':'Marker Pen',
    'price':30,
    'colors':['Red','Blue','Yellow']
}

#read
print(product)

#how to read dict values - using key
print(product['id'])
print(product['name'])
print(product['price'])
print(product['colors'])
#print(product['discount'])  #keyError
print(product.get('discount')) #None

#update

#delete