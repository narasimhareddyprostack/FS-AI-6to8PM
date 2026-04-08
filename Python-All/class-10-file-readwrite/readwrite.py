#write a py script to read - user.txt file write data into emp.txt

fp1=open('user.txt','r')
fp2=open('emp.txt','a')

data=fp1.read()
fp2.write(data)
print("New File Created successfully")

fp1.close()
fp2.close()