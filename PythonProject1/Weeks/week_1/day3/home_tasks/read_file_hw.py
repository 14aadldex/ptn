from typing import Any


def read_file():
    with open("notes.txt", "r") as file:
        readed_lines = file.readlines()
        return readed_lines


arr = read_file()
print(arr)

for line in arr:
    print(str(arr.index(line) + 1) + '. ' + line.strip())

with open("notes.txt", "a") as file:
    file.write("\nodnim gvozdei jashik, drygim ot huja hrjashik")

arr = read_file()
print(arr)

for line in arr:
    print(str(arr.index(line) + 1) + '. ' + line.strip())

print('Qnt of lines is - ' + str(len(arr)))
