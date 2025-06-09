import csv

with open('eggs.csv', 'r', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for attendance in reader:

        print(attendance["name"])
