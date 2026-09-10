import json
import os


def read_json_book():
    json_phone_book = {}
    if not os.path.exists('contact.json'):
        return {}
    try:
        with open('contact.json', 'r') as f:
            json_phone_book = json.load(f)
        return json_phone_book
    except json.JSONDecodeError as e:
        print('ошибка декодирвоания')


def safe_to_json(ph_book):
    with open('contact.json', 'w', encoding='utf-8') as file:
        json.dump(ph_book, file, indent=4)


def get_name_phone():
    name = input("Введите имя: ")
    number = input("Введите номер: ")
    return name, number
