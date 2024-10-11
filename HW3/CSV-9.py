import csv

with open('countries.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id1', 'id2', 'date'])
    for i in range(3):
        writer.writerow([i + 1, chr(97 + i), f'01/{i + 1:02d}/2019'])

with open('countries.csv', 'r') as file:
    print(file.read())
