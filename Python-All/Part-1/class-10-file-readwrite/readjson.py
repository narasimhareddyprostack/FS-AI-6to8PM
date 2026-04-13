# write a python scirpt 
# read emp.json file and print all female/male employee names
import json 
fp=open('emp.json','r')
employees=json.load(fp)


print(type(employees))
print(len(employees))

for emp in employees:
    if emp['gender']=="Male":
        print(emp['ename'])
