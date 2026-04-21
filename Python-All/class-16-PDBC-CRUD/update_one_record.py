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
            update employee set ename=%s where eid=%s
            '''
    value=("Rahul Gandhi",101)
    cursor.execute(sql_st,value)
    dbcon.commit()
    print("Data updated successfully",cursor.rowcount)

except mysql.connector.Error as err:
    print(err)