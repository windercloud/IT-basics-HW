import json

python_dict = {"name": "Artem", "age": 23, "city": "Moscow"}

json_data = json.dumps(python_dict, sort_keys=True, indent=4)

print(json_data)
