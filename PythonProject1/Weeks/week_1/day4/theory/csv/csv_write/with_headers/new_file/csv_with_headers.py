import csv

with open('one', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=("name", "age"))
    writer.writeheader()
    writer.writerow({"name": "Karl", "age": 25})
    writer.writerow({"name": "Jane", "age": 45})

with open('one', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
