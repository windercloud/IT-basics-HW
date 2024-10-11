import csv

data = [
    ['id', 'number', 'code'],
    ['1', 105, 'a5'],
    ['2', 19, 'a6'],
    ['3', 56, 'b4']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('output.csv', 'r') as file:
    print(file.read())
