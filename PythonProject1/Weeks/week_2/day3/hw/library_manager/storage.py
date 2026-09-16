import json

def read_from_file():
    books = []
    try:
        with open("books.json", "r", encoding='utf-8') as file:
            books = json.load(file)
    except FileNotFoundError:
        print("Файл не найден")
        return books
    except json.decoder.JSONDecodeError:
        print("Файл содержит некорректные данные")
        return books
    return books

def write_to_file(books):
    with open("books.json", "w", encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)