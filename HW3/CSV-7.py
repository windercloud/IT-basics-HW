import csv

columns_to_read = [0, 2]

data = []

with open('departments.csv', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        selected_columns = [row[i] for i in columns_to_read]
        data.append(selected_columns)

print(data)
