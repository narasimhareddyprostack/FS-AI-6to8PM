enames=["RG","SG","PG","Modi"]  #<class,list>
numbers=10,20,30,40   
int_numbers=range(1000)   #generate integer 0 to 999
ename="Sachin"
bytes_obj=bytes([10,20,30,255])


print("PG" in enames)   #True
print(20 in numbers)    #True
print(5 not in int_numbers) #False
print('c' in ename)         #True
print(30 not in bytes_obj)  #False
