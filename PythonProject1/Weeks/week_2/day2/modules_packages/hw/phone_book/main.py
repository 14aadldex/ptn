from utils import read_json_book, safe_to_json, get_name_phone
#испортируем функции из другого файла, сначла название файла, потом перечень


def add_contact(name, number):
    ph_book = read_json_book()
    ph_book[name] = number
    safe_to_json(ph_book)


def find_contact():
    searchable_contact = {}
    name = input("Введите имя: ")
    json_phone_book = read_json_book()
    for key in json_phone_book.keys():
        if name.lower() == key.lower():
            searchable_contact[key] = json_phone_book[key]
    return searchable_contact


def main():
    flag = True
    while flag:
        option = input("Выберите опцию:\n1. Добавить контакт \n2. Найти контакт \n3. Выйти\n")
        cast_option = 0
        try:
            cast_option = int(option)
        except ValueError:
            print("Введенное значение не является числом")
            continue
        if cast_option == 1:  # добавление в тел книгу
            name, number = get_name_phone()
            add_contact(name, number)
        elif cast_option == 2:  # поиск в тел книге
            contact = find_contact()
            if not contact:
                print("Контакт не найден")  # если пусто - то извиние
            else:
                for key, value in contact.items():
                    print(f'Контакт - {key}:{value}')
        elif cast_option == 3:  # выход
            break
        else:
            print("введено некорректное значение. попробуйте еще раз.")

#test git diff
def delete_contact():
    print("delete_contact")

if __name__ == '__main__':
    main()
