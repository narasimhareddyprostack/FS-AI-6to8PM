import csv
#Extract
fp=open("employees.csv",'r')
emp_csv_data=list(csv.reader(fp))
emp_csv=emp_csv_data[1:]  #list slicing
fp.close()
#Tranform
employees_json=[]
for emp in emp_csv:
    employees_json.append({"eid":emp[0],
                           "ename":emp[1].upper(),
                           "gender":emp[2],
                           "location":emp[3],
                           "country":"India"
                           })

print(employees_json)