numbers=[1,2,3,4,5,6,7,8,9,10]
#create new list of even numbers  [2,4,6,8,10]
#1.using filter()
#2.using without filter
#3.using filter() with lamda

even_numbers=[]

for num in numbers:
    if num%2 ==0:
        even_numbers.append(num)
        
print(even_numbers)




