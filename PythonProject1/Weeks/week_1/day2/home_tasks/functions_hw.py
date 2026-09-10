from Weeks.week_1.day1.theory.data_my_name_is import name


def calc_square(a, b):
    return a * b


square_of_five = calc_square(9, 9)
print(square_of_five)


# return few numbers
#
# def few_num(a, b):
#     sum = a + b
#     umnog = a * b
#     delen = a / b
#     razniza = a - b
#     return sum, umnog, delen, razniza
#
#
# sum, umnog, delen, razniza = few_num(5, 2)
# print(sum)
# print(umnog)
# print(delen)
# print(razniza)
#
#
# def test_with_arr(arr):
#     for item in arr:
#         print(item)
#
#
# test_with_arr([1, 2, 3, 4, 5])
# test_with_arr({'name': 'Nikki'})
# test_set = set(2.4)
# test_with_arr(test_set)  # почему он примает СЕТ????
#
#
# def some_function(*args):
#     return sum(args)
#
#
# print(some_function(1, 2, 3))


def some_function(text, **kwargs):
    print(text)
    print(kwargs)

dict = {"name": "Nikki"}
some_function("Hello World", **dict)

# some_function("Hello World", "name":'Nikki') # не понимаю, надо разбираться
