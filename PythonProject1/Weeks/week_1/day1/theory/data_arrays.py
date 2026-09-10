arr_exapmle = [1,2,3,4,5]
print(arr_exapmle)

arr_exapmle.append(9)
print(arr_exapmle)

arr_exapmle.insert(2,12)
print(arr_exapmle)

arr_exapmle.remove(3)
print(arr_exapmle)

arr_mixed = [1.0, 4, 'test']
print(arr_mixed)

arr_mixed.insert(-2,99)
del arr_mixed[-1]
print(arr_mixed)

# pop достает элемент в переменную (с ним можно работать). а в массиве он удаляется.
# может принимать аргумент индекса
# может пинимать значение в качестве агрумента когда работаем со строкой.
pop_array = [1,2,3,4,5]
poped_element = pop_array.pop()
print(poped_element)
poped_element = pop_array.pop(2)
print(pop_array)
print(poped_element)
