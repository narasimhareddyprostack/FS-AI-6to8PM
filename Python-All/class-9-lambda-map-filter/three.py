a=100

""" wish=lambda ename,esal:"Hello-"+ename+"-Employee Salary:"+str(esal)

 """

def wish(ename,esal):
    msg="Hello-"+ename+"-Employee Salary:"+str(esal)
    return msg

msg=wish("Rahul",45000.45)   #TypeError
print(msg)