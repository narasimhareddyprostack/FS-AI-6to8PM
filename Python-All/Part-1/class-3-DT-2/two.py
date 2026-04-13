#Create
enames=("Rahul","Sonia","Priya")

#Read
print(enames)
#read tuple elements- using
print(enames[0])  #Rahul
#print(enames[9])  #Index Error

#update
#enames[0]="Rahul Gandhi"   #TypeError:'tuple' object does not support item assignment
print(enames)

#delete Tuple Elements
del enames[0]