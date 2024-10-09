import json

python_dict = {"name": "Artem", "age": 23}
python_string = "Hello, JSON!"
python_int = 100
python_bool = True

json_dict = json.dumps(python_dict)
json_string = json.dumps(python_string)
json_int = json.dumps(python_int)
json_bool = json.dumps(python_bool)

print(json_dict)
print(json_string)
print(json_int)
print(json_bool)