from storage import read_from_file, write_to_file
from logic import casting_input, add_book, show_books, find_book_by_author, mark_as_readed, statistics, delete_book


def main():
    flag = True
    books = read_from_file()
    while flag:
        cast_input = 0
        user_input = input("Выберите опцию: \n1. Добавить книгу (название, автор, год, жанр) \n2. "
                           "Показать все книги\n3. Найти книги по автору \n4. Отметить книгу как прочитанную "
                           "\n5. Показать статистику (сколько всего, сколько прочитано, средний год)\n6. Удалить книгу\n7. Выход\n")
        cast_input = casting_input(user_input)
        if cast_input is None:
            continue
        if cast_input == 1:  # 1. Добавить книгу (название, автор, год, жанр) /готоВо
            books = add_book(books)
            write_to_file(books)
        elif cast_input == 2:  # 2. Показать все книги /готово
            result_arr = show_books(books)
            for book in result_arr:
                print(book)
        elif cast_input == 3:  # 3. Найти книги по автору
            user_input_author = input("Введите пожалуйста фамилию автора: ")
            result = find_book_by_author(books, user_input_author)
            if len(result) <= 0:
                print("нет найденных результатов")
            else:
                books = show_books(result)
                for book in books:
                    print(book)
        elif cast_input == 4:  # 4. Отметить книгу как прочитанную /готово
            result_arr = show_books(books)
            for book in result_arr:
                print(book)
            user_input_readed_book = input("ведите название книги которую вы прочитали: ")
            books = mark_as_readed(books,user_input_readed_book)
            write_to_file(books)
        elif cast_input == 5:  # 5. Показать статистику (сколько всего, сколько прочитано, средний год)
            avg_year, readed_books_qnt, total_books = statistics(books)
            print(
                f'средний год: {avg_year}, всего прочитано: {readed_books_qnt}, всего книг в библиотеке: {total_books}')
        elif cast_input == 6:  # 6. Удалить книгу /готово
            book_index = input("Введите номер книги: ")
            books = delete_book(books, book_index)
            write_to_file(books)
        elif cast_input == 7:  # 7. Выход /готово
            break
        else:
            print('Выбран несуществующий вариант - ' + str(cast_input))


if __name__ == "__main__":
    main()
