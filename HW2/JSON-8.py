import json

def parse_complex(obj):
    return complex(obj['real'], obj['img']) if '__complex__' in obj else obj

complex_object = json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook=parse_complex)
simple_object = json.loads('{"real": 4, "img": 3}', object_hook=parse_complex)

print("С комплексными объектами:", complex_object)
print("Без комплексных объектов:", simple_object)
