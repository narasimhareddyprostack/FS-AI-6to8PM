#Extract data from Rest API
import requests,csv,mysql.connector,json,pymongo

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


#Load data into mysql Table 
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='6pm')
    cursor=dbcon.cursor()
    sql_st='''
            insert into products(pid,pname,price,category,rating) values(%s,%s,%s,%s,%s); 
           ''' 
    cursor.executemany(sql_st,beauty_products_csv)
    dbcon.commit()
    print('Data inserted into product Table successfully-',cursor.rowcount)

except mysql.connector.Error as err:
    print(err)

#Load data into new json file 

fp2=open('productt.json','w')
json.dump(beauty_products_json,fp2)
print("New JSON File Created successfully")


#load data into mongodb collection


try:
    client=pymongo.MongoClient('mongodb://localhost:27017/') 
    db=client['6pm']
    product_col=db['products']
    product_col.insert_many(beauty_products_json)
    print("Data inserted into MongoDB collection successfylly")

except Exception as err:
    print(err)