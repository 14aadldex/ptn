# 1. списки (сделать список из 100 случ чисел), написать
# фильт который оставит только четные. отсортировать по возрастанию и убываню
import random


def main():
    num_arr = gen_num(100)  # сделать список из 100 случ чисел
    print(num_arr)
    even_arr = return_even_num_from_arr(num_arr)
    print(sort_arr(even_arr, 1))
    print(sort_arr(even_arr, 0))


# сделать список из 100 случ чисел
def gen_num(limit):
    arr = []
    for i in range(limit):
        arr.append(
            random.randint(1, 50000))  # randint принимает диапазон и возвращает случ число в диапазоне, вклю границы
    return arr


# возвращает только четные числа в новом массиве
def return_even_num_from_arr(arr):
    even_arr = []
    for num in arr:
        if num % 2 == 0:
            even_arr.append(num)
    return even_arr


def sort_arr(arr, dest):
    if dest == 1:
        return sorted(arr)
    else:
        return sorted(arr, reverse=True)


main()
