import csv

fp1=open("user.csv",'r')
csv_data=csv.reader(fp1)
user_data=list(csv_data)
print(len(user_data[1:]))
print(user_data[1:])