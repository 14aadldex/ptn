import csv
import random
import string


# задача сделать генератор паролей и сохранить в файл с новой строки

# метод в цикле склеивает полученные числа
def pass_gen(index):
    total = ''
    for i in range(index):
        total = total + str(get_one_num_and_letter())
    return total


# генерит по 1 андомному числу и букве.
def get_one_num_and_letter():
    num = format(random.random(), '.1f')
    num = str(int((float(num) * 9)))
    let = random.choice(string.ascii_letters)
    return num + let


with open('blacklist.txt', 'a+', newline='') as file:
    file.write('\n' + pass_gen(4))

# for line in file:

# print(pass_gen(4))
