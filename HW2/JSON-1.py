import json
json_data = '{"name":"Artem", "age":"23"}'
python_obj = json.loads(json_data)
print(f"Name: {python_obj['name']}")
print(f"Age: {python_obj['age']}")