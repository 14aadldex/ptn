import csv
import json

from Weeks.week_1.day3.theory.csv_read import writer

books = '[{"name": "Дуб зеленый",    "author": "Пушкин",    "date": "1678"},{    "name": "Преступление и наказание",    "author": "Достоевский",    "date": "1866"}]'

json_my = json.loads(books)
for item in json_my:
    print(item["name"])
    print(item["author"])
    print(item["date"])

with open('hw.json', 'w', encoding='utf-8') as file:
    json.dump(json_my, file, ensure_ascii=False, indent=4)

data_price = [{"name": "apple", "price": 25.24, "qnt": "23"},{"name": "banana", "price": 15.32, "qnt": "12"},{"name": "pine", "price": 55.32, "qnt": "7"}]
with open('books.csv', 'w', encoding='utf-8', newline='') as file:
    headers = ['name', 'price', 'qnt']

    writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')
    writer.writeheader()
    writer.writerows(data_price)
