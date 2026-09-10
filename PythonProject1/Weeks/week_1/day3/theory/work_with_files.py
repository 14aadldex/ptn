file = open("text.txt", "x")  # r - read. w- write. a -append. x - create, got an error if file Exist.
file.write("do not open, your now who inside")
file.close()  # need to close file in the end of work with it

with open("text.txt", "r") as file:
    date = file.read()
    # file will be closed automatically

with open("text.txt", "a") as file:
    file.write('\ntext after text')
    # file.write('\nТест русского текста без ЮТФ8')

with open("text.txt", "r", encoding='utf-8') as file:
    file = file.readlines()
    print(file)
