book_attribute = ['название', 'автор', 'год', 'статус']

def find_book(books):
    res = input("введите название книги которую ищите: ").lower()
    res = res.replace('\n', '').replace('\r', '')
    for book in books:
        if res in book[book_attribute[0]].lower():
            print(book)

def main():
    books = read_file_library()
    flag = True
    while flag:
        result = str(input(
            '1. Показать все книги\n2. Добавить книгу\n3. Найти книгу\n4. Удалить книгу\n5. Выйти\nВыберите цифру действие: '))
        if result == "5":
            break
        elif result == "4":
            del_book(books)
        elif result == "3":
            find_book(books)
        elif result == "2":
            add_book(books)
        elif result == "1":
            load_books(books)
        else:
            print("<---Некорректный ввод--->")


# читаем тест файл и записываем в массив в памяти
def read_file_library():
    books_array = []
    with open("library.txt", "r", encoding="utf-8", newline="") as file:
        for line in file:
            if not line:
                continue
            book_by_fields = line.split("|")
            book = {}
            for key in book_attribute:
                book.setdefault(key, book_by_fields[book_attribute.index(key)])
            books_array.append(book)
    return books_array


# проходит по массиву словарей и выводит в консоль каждую книгу с ключ значение. Шаг 1 в задаче.
def load_books(books):
    for item in books:
        book_for_print = ''
        for key, value in item.items():
            book_for_print += f'{key}|{value}|'
        print(str(books.index(item) + 1) + '. ' + book_for_print)
        print("---------")


def del_book(books):
    flag = True
    while flag:
        index_book_for_deleting = ""
        load_books(books)
        try:
            index_book_for_deleting = input("Введите номер книги который хотите удалить: ")
            index_book_for_deleting = int(index_book_for_deleting)
        except ValueError:
            print("Это не число")
            continue
        if index_book_for_deleting > len(books):
            print("Некорректный ввод, введеное число больше чем есть книг в библиотеке")
            continue
        total_index = int(index_book_for_deleting) - 1
        books.pop(total_index)
        save_books(books)
        print("Книга была удалена")
        flag = False


# запрашивает у пользователя данные по книге и добавляет их в общую библиотеку. последний параметр всегда "в наличии"
def add_book(books):
    book = {}
    for item in book_attribute[:-1]:
        user_input = input(f"Введите {item} книги: ").strip()
        book.setdefault(item, user_input)
    book['статус'] = 'В наличии'
    books.append(book)  # добавляю в локальный словарь
    save_books(books)  # записываю в файл


# записываем книги из Словаря в текст файл (полностью обновляя файл txt)
def save_books(books):
    with open("library.txt", "w", encoding="utf-8", newline="") as file:  #
        for item in books:
            result_string = ''
            for value in item.values():
                result_string += f'{value}|'
                result_string = result_string.replace('\n', '').replace('\r','')  # удаляю все переносы строк и каретки если они там были (чтобы в файл писалось одной строкой)
            result_string += '\n'
            file.write(result_string)


# start app
main()
