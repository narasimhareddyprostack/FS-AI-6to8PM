import csv

fp=open("employees.csv",'r')
emp_csv_data=list(csv.reader(fp))
print(emp_csv_data)
emp_csv=emp_csv_data[1:]  #list slicing
print(emp_csv)

fp.close()