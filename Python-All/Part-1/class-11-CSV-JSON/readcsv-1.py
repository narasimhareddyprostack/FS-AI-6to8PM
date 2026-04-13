import csv

fp1=open("user.csv",'r')
csv_data=csv.reader(fp1)
user_data=list(csv_data)
print(type(csv_data))
print(type(user_data))