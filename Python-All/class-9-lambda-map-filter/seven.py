numbers=[1,2,3,4,5,6,7,8,9,10]
#create new list of even numbers  [2,4,6,8,10]
#1.using filter()
#2.using without filter
#3.using filter() with lamda

#print(list(filter(lambda num:num%2==0,numbers)))
def check_num(num):
    return num%2==0


filter_obj=filter(check_num,numbers)
even_numbers=list(filter_obj)
print(even_numbers)




