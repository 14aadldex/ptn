# 1. напиши код который просит юзера ввести число
# 2. оберни каст инпута в try except
# 3. else если нет ошибок. и finally (для закрытия файла)
# 4. сломай прогу и почини try\except

num = input("введи число: ")
with open('one_q.txt', 'w', newline='') as file:
    try:
        number = int(num)
    except ValueError:
        print('not a number')
    else:
        print(number)
        file.write(num)
    finally:
        print('finally')