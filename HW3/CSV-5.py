import csv

data = []

with open('departments.csv', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Удаляем начальные пробелы из каждого элемента
        row = [element.lstrip() for element in row]
        data.append(row)

print(data)
