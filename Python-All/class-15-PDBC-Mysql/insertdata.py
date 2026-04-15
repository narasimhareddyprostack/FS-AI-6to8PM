import mysql.connector

dbcon=None
cursor=None 

try:
    dbcon=mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="root",
                                 database="6pm")
    cursor=dbcon.cursor()
    sql_st='''
            insert into employee(eid,ename,esal) values(101,'Rahul',45000.45);
           '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(err)