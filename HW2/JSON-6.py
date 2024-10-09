import json

with open('names.json') as file:
  names = json.load(file)

with open('new-names.json') as file:
  json.dump(names, file)
  
# У меня нет никакого файла json,
# чтобы вытащить оттуда данные.
# Но программа выглядела бы так,
# если бы мы не вносили изменения в names