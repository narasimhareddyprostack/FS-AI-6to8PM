import mysql.connector

dbcon=None
cursor=None 

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='6pm') 
    cursor=dbcon.cursor()
    sql_st='''
            create table employee(
            	eid int primary key,
	            ename varchar(32) not null,
	            esal float,
	            loc varchar(32) default 'Bangalore',
	            gender varchar(32) 
            );
           '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("New Table Created")

except mysql.connector.Error as err:
    print(err) 
