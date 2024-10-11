import csv

data = []

with open('employees.csv', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

print(data)
