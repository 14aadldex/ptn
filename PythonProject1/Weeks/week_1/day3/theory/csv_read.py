import csv

# with open('data.csv') as csv_file:
#     reader = csv.reader(csv_file)
#
#     for row in reader:
#         # print(row)
#
#         if row[0]=='John':
#             print(row)
#         else:
#             print('it doesnt matter')
#
# #read with file headers
# print('read with file headers')
# with open('data.csv') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['Name'], row['Age'])

# write in csv

data2 = [['Name', 'Age', 'City'], ['Serg', '22', 'Vologda'], ['Evgen', '45', 'Tula']]

with open('data2.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Cost', 'Size'])
    # writer.writerows(data2)

with open('data2.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

data3 = [{'Name':"Serg", 'Age':"25", 'City':"Monako"},{'Name':"Mike", 'Age':"15", 'City':"Sarav"},{'Name':"Bill", 'Age':"55", 'City':"Carerros"}, ]

with open('data2.csv', 'w', newline='') as csv_file:
    fieldnms = ['Name', 'Age', 'City']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnms, delimiter=';')
    writer.writeheader()
    writer.writerows(data3)
