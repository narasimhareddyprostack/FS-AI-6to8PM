import mysql.connector

dbcon=None
cursor=None 

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='6pm') 
    cursor=dbcon.cursor()
    sql_st='''
            insert into employee values(%s,%s,%s,%s,%s);
            
           '''
    data=[
        (102,'Sonia',55000.55,'New Delhi','Female'),
        (103,'Priyanka',55000.55,'New Delhi','Female'),
        (104,'Modi',55000.55,'Bangalore','Male'),
        (105,'Alia',65000.55,'Bangalore','Female'),
        (106,'Amith',75000.55,'New Delhi','Male'),
        (107,'Vijay',85000.55,'Chennai','Male'),
        (108,'Sachin',95000.55,'Chennai','Male'),
        (109,'Surya',35000.55,'Chennai','Male'),
        (110,'Pawan',15000.55,'New Delhi','Male')
        
    ]
    cursor.executemany(sql_st,data)
    dbcon.commit()
    print(cursor.rowcount,"Record(s) inserted")

except mysql.connector.Error as err:
    print(err) 
