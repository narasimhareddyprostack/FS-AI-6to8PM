import mysql.connector
dbcon=None
cursor=None 
try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",
                                 database="6pm")
    cursor=dbcon.cursor()
    sql_st='''
            insert into employee(eid,ename,esal) values(%s,%s,%s);
           '''
    emp_data=[(102,'Sonia',65000.65),
              (103,'Priyanka',75000.75),
              (104,'Modi',85000.75),
              (105,'Amith',95000.75),
              (106,'Rajni',75000.75),
              ]
    cursor.executemany(sql_st,emp_data)
    dbcon.commit()
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(err)