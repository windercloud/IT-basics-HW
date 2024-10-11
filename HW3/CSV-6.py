import csv

data = []

with open('countries.csv', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        row = [element.strip().replace('"', '').replace("'", "") for element in row]
        data.append(row)

print(data)
