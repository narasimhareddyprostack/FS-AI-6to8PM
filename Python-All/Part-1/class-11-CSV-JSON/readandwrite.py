import csv
import json
#Extract
fp1=open("user.csv",'r')
csv_data=csv.reader(fp1)
user_data=list(csv_data)
users_csv=user_data[1:]  #excluding index 0 element using list slicing
print(users_csv)

#transform
users_json=[]
for user_list in users_csv:
    users_json.append({"uid":int(user_list[0]),"uname":user_list[1],"gender":user_list[2]})

print(users_json)



#Load into -new json file

fp2=open('user.json','w')
json.dump(users_json,fp2)

print("New JSON File Created")