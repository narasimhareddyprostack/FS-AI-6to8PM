#write a python script
#read user.json file and          
# 1.write all male employee into male.json
# 2.write all female employee into female.json

import json 
fp1=open('user.json','r')
fp2=open('male.json','w')
fp3=open('female.json','w')

users=json.load(fp1)

def verify_gender(user):
    return user['gender']=="Female"

male_employees=list(filter(lambda user:user['gender']=='Male',users))
female_employees=list(filter(verify_gender,users))
#print(len(male_employees))
print(len(female_employees))

json.dump(male_employees,fp2)
json.dump(female_employees,fp3)
print("New JSON File created")