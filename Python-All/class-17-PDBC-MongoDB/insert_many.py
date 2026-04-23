#Write a python script to 
#insert one document in mongodb collection.
import pymongo

try:
    client=pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['6pm']
    emp_col=db['emp']
    employees=[
        {"eid":101,"ename":"Rahul1","esal":45000},
        {"eid":102,"ename":"Rahul2","esal":45000},
        {"eid":103,"ename":"Rahul3","esal":45000},
        {"eid":104,"ename":"Rahul4","esal":45000},
        {"eid":105,"ename":"Rahul5","esal":45000},
        {"eid":106,"ename":"Rahul6","esal":45000},
        {"eid":107,"ename":"Rahul7","esal":45000},
        {"eid":108,"ename":"Rahul8","esal":45000},
        {"eid":109,"ename":"Rahul9","esal":45000},
        {"eid":110,"ename":"Rahul10","esal":45000},
        {"eid":111,"ename":"Rahul11","esal":45000},
    ]
    emp_col.insert_many(employees)
    print("Document Inserted Successfully")

except Exception as err:
    print(err)
