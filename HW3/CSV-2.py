import csv

with open('countries.csv', newline='') as csvfile:
    for row in csv.reader(csvfile, delimiter='\t'):
        print(row)
