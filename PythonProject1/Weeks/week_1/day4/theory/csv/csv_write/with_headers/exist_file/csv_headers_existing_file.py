import csv

with open('one', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age'])
    writer.writerow({'name': 'Andrey', 'age': 74})

with open('one', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)