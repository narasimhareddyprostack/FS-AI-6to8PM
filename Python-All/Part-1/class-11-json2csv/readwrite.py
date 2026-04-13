import json 
import csv
#Extract
fp1=open('emp.json','r')
employees=json.load(fp1)
print(type(employees))
#print(employees)


#Transfor for csv file
employees_csv=[]
for emp in employees:
    employees_csv.append([emp['id'],emp['name'],emp['address']['city']])

print(employees_csv)
#Load
fp2=open('emp.csv','w',newline="")
csv_writer=csv.writer(fp2)
csv_writer.writerow(['Uid','User Name','City'])
csv_writer.writerows(employees_csv)

print("New CSV File Created")