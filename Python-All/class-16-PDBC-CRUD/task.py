#read csv file. Write data into new json file.
import csv, json
fp1=open("employee.csv", "r")
employee_csv_data=csv.reader(fp1)
employees=list(employee_csv_data)
print(employees)

employee_jason=[]
for employee in employees[1:]:
    employee_jason.append({"empid":employee[0],"ename":employee[1]})


fp2=open("employee.json", "w")
json.dump(fp1(employee_jason))