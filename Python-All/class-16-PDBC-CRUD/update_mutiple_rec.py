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
          update employee
          set ename=%s
          where eid=%s
    '''
    values=[
           ("Sonia Gandhi",102),
           ("Priyanka Gandhi",103),
           ("Narendra Modi",104),
           ("Alia Bhut",105)
           ]
    cursor.executemany(sql_st,values)
    dbcon.commit()
    print("Data updated successfully",cursor.rowcount)

except mysql.connector.Error as err:
    print(err)

finally:
    cursor.close()
    dbcon.close()