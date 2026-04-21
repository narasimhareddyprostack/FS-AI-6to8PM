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
        delete from employee where gender=%s;
    '''
    value=[("Female")]
    cursor.execute(sql_st,value)
    dbcon.commit()
    print(cursor.rowcount,"No of row(s) deleted successfully")

except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()