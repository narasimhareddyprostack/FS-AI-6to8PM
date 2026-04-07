numbers=[10,20,30,40]
#create new list of numbers by adding plus 1
#1. with map
#2. with out map
#3. wit map with lamba

def addplus(num):
    return num+1

map_obj=map(addplus,numbers)
new_numbers=list(map_obj)

print(numbers)
print(new_numbers)