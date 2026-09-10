# base
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 21,
    'city': 'New York'
}
print(f'my name is {person["first_name"]} '
      f'{person["last_name"]}, i am {person["age"]} years old, and living in {person["city"]}')

# sum_count
prices = {
    "bread": 45,
    "milk": 112,
    "aggs": 68
}
sum_of_products = 0
for key, value in prices.items():
    sum_of_products += value
    if value > 100:
        print(f'This {prices[key]} cost is more than 100, actually -' + str(prices[key]))
print(str(sum_of_products) + ' total prices')

# phonebook
# phonebook = {}
#
# flag = True
# while flag:
#     user_input = input("please enter 'add' or 'exit' ")
#     if user_input == 'add':
#         name = input("please enter name ")
#         phone = input("please enter phone number ")
#         phonebook[name] = phone
#     elif user_input == 'exit':
#         flag = False
# print(phonebook)

# task with *
student = [{"name": "Ann", "Grade": "75"}, {"name": "Johm", "Grade": "52"}, {"name": "Kate", "Grade": "99"}]

average_grade = 0.0
length = len(student)

for item in student:
    average_grade += int(item["Grade"])

total = int(average_grade / length)
print('average grade - ' + str(total))
print("")

for item in student:
    print(item['name'] + ', grade -' + item["Grade"])
    if int((item["Grade"])) == total:
        print("Srednii")
        print("")
    elif int((item["Grade"])) > total:
        print("Vishe Srednego")
        print("")
    elif int((item["Grade"])) < total:
        print("Nige Srednego")
        print("")
# print(format(num, '.3f'))
