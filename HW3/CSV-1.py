import csv

with open('departments.csv', newline='') as csvfile:
    for row in csv.reader(csvfile):
        print(row)
