numbers=[10,20,30,40]
#create new list of numbers by adding plus 1
#1. with map
#2. with out map
#3. with map with lamba

new_numbers=list(map(lambda num:num+1,numbers))

print(numbers)
print(new_numbers)