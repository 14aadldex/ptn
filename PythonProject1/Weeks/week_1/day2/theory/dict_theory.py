student = {
    "name": "Alex",
    "age": 33,
    "height": 178,
    "weight": 76
}

print(student)

print(student.get("names")) # безопасный поиск в словаре. если нет элемента вернет NONE
print(student["name"]) # не безопасный, если нет ключа упадет в ошибку

student['country'] = 'Russia' #добавление, если элеменат нет - добавит. если есть обновит значение
print(student)

student['country'] = 'Belorussia' #добавление, если элеменат нет - добавит. если есть обновит значение
print(student)

country = student.setdefault('country','Nigeria')
print(student)
print(country)
print('-----------------')
for key in student.keys():
    print(key)
print('-----------------')
for value in student.values():
    print(value)
print('-----------------')
for key, value in student.items():
    print(f'{key} = {value}')