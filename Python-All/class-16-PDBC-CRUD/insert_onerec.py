import mysql.connector

dbcon=None
cursor=None 

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='6pm') 
    cursor=dbcon.cursor()
    sql_st='''
            insert into employee(eid,ename,esal,loc,gender)
            values
            (101,'Rahul',45000.45,'Bangalore','Male');
            
           '''
    cursor.execute(sql_st)
    dbcon.commit()
    print(cursor.rowcount,"Record(s) inserted")

except mysql.connector.Error as err:
    print(err) 
