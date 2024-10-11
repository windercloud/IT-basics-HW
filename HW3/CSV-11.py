import csv

data = {
    'id': ['1', '2', '3'],
    'Age': [105, 19, 56],
    'City': ['a5', 'a6', 'b4']
}

with open('output2.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    writer.writeheader()
    for i in range(len(data['id'])):
        writer.writerow({key: data[key][i] for key in data.keys()})

with open('output2.csv', 'r') as file:
    print(file.read())