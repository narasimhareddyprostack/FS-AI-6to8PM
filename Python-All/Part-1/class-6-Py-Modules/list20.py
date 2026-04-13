import random


numbers=[101,201,301,11,7,8,18,31,1055,232,4,7,199,299,399,499,599,699,799,899]
print(len(numbers))

print(random.choices(numbers,k=5))
print(random.choice(numbers))