import string
import random

allchar=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
#print(allchar)

pwd=''
for element in range(10):
    pwd=pwd+random.choice(allchar)

print(pwd)