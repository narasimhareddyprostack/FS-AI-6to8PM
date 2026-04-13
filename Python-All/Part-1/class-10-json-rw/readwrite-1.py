#write a python script
#read user.json file and          
# 1.write all male employee into male.json
# 2.write all female employee into female.json

import json 
fp1=open('user.json','r')
fp2=open('male.json','w')
fp3=open('female.json','w')

users=json.load(fp1)
print(len(users))
print(type(users))

