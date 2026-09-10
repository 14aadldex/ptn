user = {
    'name': 'Karl',
    'age': 20,
    'citizenship': 'USA'
}

print(user)

print(user.get('Pname', 'unknown'))

#если нет то добавить
print(user.setdefault('size', 'XL'))

print(user)

user['age'] = 30
user['job'] = 'Engineer'

print(user)

roles = {
    'job': 'Engineer',
    'grade': 'Senior'
}

#обьединение двух словарей. повторяющиеся обьедин в одну. уникальные просто добавляются.
user.update(roles)
print(user)

# удаление из словаря

user.pop('grade') # del last element
print(user)

lstitem = user.popitem() #del list elem and put in Variable
print(user)

print(f'Last element in dic was {lstitem}')

# delete element by name
del user['age']
print(user)

#exception in case del NOt existing element
# del user['citizenship1']

#generate arr from dictionaty
keys_list = user.keys()
print(keys_list)
print(user.values())


