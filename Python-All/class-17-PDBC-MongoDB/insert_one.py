#Write a python script to 
#insert one document in mongodb collection.
import pymongo

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['6pm']
    emp_col=db['emp']
    emp_col.insert_one({"eid":101,"ename":"Rahul"})
    print("Document Inserted Successfully")

except Exception as err:
    print(err)
