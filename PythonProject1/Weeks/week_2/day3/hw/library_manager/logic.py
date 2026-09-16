from storage import write_to_file


def statistics(books):  # Показать статистику (сколько всего, сколько прочитано, средний год)
    average_year = 0
    count_readed = 0
    total_books = len(books)
    if books:
        for book in books:
            if book['read']:
                count_readed += 1
            average_year += book['year']
        if total_books > 0:
            average_year /= total_books
    return average_year, count_readed, total_books


def mark_as_readed(books, user_input_readed_book):
    for book in books:
        if book['title'].lower() == user_input_readed_book.lower():
            book['read'] = True
    return books


def delete_book(books, book_index):
    cast_book_index = 0
    try:
        cast_book_index = casting_input(book_index) - 1
        if len(books) > cast_book_index:
            books.remove(books[cast_book_index])
    except ValueError:
        print("Введено не числовое значение. Попробуйте еще раз")
    return books


def show_books(books):
    str_books = []
    for book in books:
        index = books.index(book) + 1
        result_string = ''
        for key, value in book.items():
            result_string += f"{key}: {value} ,"
        str_books.append((str(index) + ". " + result_string))
    return str_books


def add_book(books):
    new_book = {}
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год выпуска книги: ")
    genre = input("Введите жанр книги: ")
    read = input("Вы уже прочитали эту книгу? y/n: ")
    new_book["title"] = title
    new_book["author"] = author
    new_book["year"] = casting_input(year)
    new_book["genre"] = genre
    if read == "y":
        new_book["read"] = True
    else:
        new_book["read"] = False
    books.append(new_book)
    return books


def find_book_by_author(books, user_input_author):
    searchable_books = []

    for book in books:
        if user_input_author.lower() in book["author"].lower():  # есть ли частичное вхождение
            searchable_books.append(book)
    return searchable_books


def casting_input(user_input):
    try:
        user_input_integer = int(user_input)
        return user_input_integer
    except ValueError:
        print("Введено не числовое значение из меню. Попробуйте еще раз")
        return None
