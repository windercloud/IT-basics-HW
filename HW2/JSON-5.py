import json

json_dict = {"name":"Artem", "age":23, "city":"Moscow"}
json_bool = (True)
json_int = (100)

python_dict = json.dumps(json_dict)
python_bool = json.dumps(json_bool)
python_int = json.dumps(json_int)

print(python_dict)
print(python_bool)
print(python_int)

