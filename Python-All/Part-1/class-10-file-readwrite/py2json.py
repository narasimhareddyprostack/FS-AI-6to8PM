import json 


emp={'eid': 101, 'ename': 'Rahul', 'avail': True}
print(type(emp))

emp_json_str=json.dumps(emp)
print(emp)
print(emp_json_str)