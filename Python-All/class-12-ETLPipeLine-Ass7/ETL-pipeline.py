import csv,json
#Extract
fp1=open("employees.csv",'r')
emp_csv_data=list(csv.reader(fp1))
emp_csv=emp_csv_data[1:]  #list slicing
fp1.close()
#Tranform
employees_json=[]
for emp in emp_csv:
    employees_json.append({"eid":emp[0],
                           "ename":emp[1].upper(),
                           "gender":emp[2],
                           "location":emp[3],
                           "country":"India"
                           })
#Load data in new json file
fp2=open('employees-output.json','w')
json.dump(employees_json,fp2)
print("New JSON File Created")