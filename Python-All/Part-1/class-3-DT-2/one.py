#Create List Object
enames=["Rahul","Sonia","Priya"]

#Read list 
print(enames)

#Read List elements - using indexing
print(enames[0])  #Rahul
#print(enames[9])  #IndexError

#update
enames[0]="Rahul Gandhi"
print(enames)

#Delete
del enames[0]
print(enames)