from math import trunc
from operator import truediv

string = 'Olegaaa \n\tKoooostik'
print(string)

string_1 = ' test with spaces'
string_2 = 'test with spaces '
string_3 = ' test with spaces '

print(string_1)
print(string_2)
print(string_3)

print("empty line_______")

print(string_1.lstrip()) # удалет пробел слева
print(string_2.rstrip()) # удалет пробел справа
print(string_3.strip()) # удаляет пробел и слева и справа

numb = 36
print("My age is " + str(numb)) #обязательно приведение типов


boolean = True
boolean = False
print(boolean)

test_double = 12.2
print(test_double)

print( type(test_double)) #type() вертнет к какому классу относится переменная
print(type(numb))
print(type(string_1))
print(type(boolean))

#integer = int(input())
#print(integer)