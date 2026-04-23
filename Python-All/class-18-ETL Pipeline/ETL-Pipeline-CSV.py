#Extract data from Rest API
import requests,csv

resp=requests.get('https://dummyjson.com/products')
products=resp.json()['products']


#Tranform - data for CSV file,mysql Table
beauty_products_csv=[]
#Tranform - data for JSON file and MongoDB Collection
beauty_products_json=[]

for product in products:
    if product['category']=="beauty":
        beauty_products_csv.append((product['id'],
                                    product['title'],
                                    product['price'],
                                    product['category'],
                                    product['rating']
                                    ))
        beauty_products_json.append({'pid':product['id'],
                                     'pname':product['title'],
                                     'price':product['price'],
                                     'category':product['category'],
                                     'rating':product['rating']
                                     })


#Load data into csv file 
fp1=open('products.csv','w')
csv_writer=csv.writer(fp1)
#writing CSV Header
csv_writer.writerow(['pid','pname','price','category','rating'])  
#writeting data into csv file 
csv_writer.writerows(beauty_products_csv)
print("New CSV File Created Successfully")