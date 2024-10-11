import csv

data = []

with open('departments.csv', newline='') as file:
    csv_reader = csv.reader(file)
    field_names = next(csv_reader)
    for row in csv_reader:
        data.append(row)

print("Названия полней:", field_names)
print("Количество рядов:", len(data))
