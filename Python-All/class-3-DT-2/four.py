#set is mutable object

#create 
eids={101,101,101,101,101}   #set  - duplicates are not allowed
s1={10,20.5,"Rahul",True}
#read
print(eids)  #{101}
print(s1)    #{"Rahul",True,10,20.5}
  
#update
eids.add(102)
print(eids)
#delete
eids.clear()
print(eids)