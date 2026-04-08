fp=open('data.txt','r')


#display all file pointer properties

print(fp.name)   #data.txt
print(fp.mode)   #read
print(fp.readable())  #True
print(fp.writable())  #False

print(fp.closed)   #False