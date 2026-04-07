def wish(ename):
    return "Hello:"+ename

msg=wish("Rahul")
print(msg)


wish = lambda ename:"Hello:"+ename

msg=wish("Rahul")
print(msg) 