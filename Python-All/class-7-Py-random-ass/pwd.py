import string
import random
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

allchar=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
print(allchar)

print(random.choice(allchar))

pwd=''
for element in range(10):
    pwd=pwd+random.choice(allchar)

print(pwd)