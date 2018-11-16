import csv

with open('Minorenkeuze.csv', 'r') as csv_file:
    csvreader = csv.reader(csv_file)

    print(csv_reader)
