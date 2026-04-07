enames=['rahul','sonia','priya','rajni','amith','raj','satya']

#collect all employees their name start with 'r';

new_enames=list(filter(lambda ename:ename.startswith('s'),enames))
print(new_enames)
