enames=['rahul','sonia','priya','rajni','amith','raj']

#collect all employees their name start with 'r';

def verify_name(ename):
    return ename.startswith('r')

filter_obj=filter(verify_name,enames)
new_enames=list(filter_obj)
print(new_enames)
