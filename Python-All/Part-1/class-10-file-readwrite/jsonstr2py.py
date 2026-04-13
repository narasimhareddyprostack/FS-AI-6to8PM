import json 


emp_json_str='''
                {"eid":101,"ename":"Rahul","avail":true}
              '''

emp=json.loads(emp_json_str)
print(emp)

#               {'eid': 101, 'ename': 'Rahul', 'avail': True}