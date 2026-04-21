import mysql.connector

dbcon=None
cursor=None 

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='6pm') 
    cursor=dbcon.cursor()
    sql_st="select *from employee"
    cursor.execute(sql_st)
    employees=cursor.fetchall()


    for emp in employees:
        print(emp[1])

except mysql.connector.Error as err:
    print(err) 

finally:
    cursor.close()
    dbcon.close()