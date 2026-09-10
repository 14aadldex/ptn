cars = ['vax', 'haval', 'bmw', 'ford', 'geely']

appender_text = 'best car in the world - '
for item in cars:
    print(f'{appender_text}' + item )

# магия цикла с возведением в квадрат в диапазоне до 10, при этом создается словарь на лету
sqlite3 = {x:x**2 for x in range(10)}
print(sqlite3)

items_arr = []
for x in range(10):
    items_arr.append("Name" + str(x))

print(items_arr)