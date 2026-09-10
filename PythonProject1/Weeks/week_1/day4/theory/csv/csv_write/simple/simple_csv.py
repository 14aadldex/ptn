import csv

with open('simp_csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['a','b','c'])
    csv_writer.writerow(['d','e','f'])

with open('simp_csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)