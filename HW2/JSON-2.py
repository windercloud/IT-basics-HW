import json
python_obj = {
  "name": "Artem",
  "age": 23
}

json_data = json.dumps(python_obj)

print(json_data)