numbers=[10,20,30,40]

#create new list of numbers by adding +1
#new_numbers= [11,21,31,41]

def addplus_one(num):
    return num+1

#new_numbers=list(map(lambda num:num+1,numbers))
new_numbers=list(map(addplus_one,numbers))
print(numbers)
print(new_numbers)

#for every eelement of list, executing fun