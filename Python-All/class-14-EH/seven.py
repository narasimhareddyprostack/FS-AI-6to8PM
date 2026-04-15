fp=None
try:
    fp=open("data.txt",'r')
    data=fp.read()
    print(data)

except FileNotFoundError as err:
    print(err)

finally:
    print("finally Block will execute always")
    fp.close()


print("GE")