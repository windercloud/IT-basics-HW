import csv

data = []

with open('departments.csv', newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

print(data)
