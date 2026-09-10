arr = set(range(0,100))
print(arr)

#find max
print(max(arr))

max_num = 0
for num in arr:
    if num >max_num:
        max_num = num
print(max_num)

#elemnets index
arr_fruits = ['apple', 'banana', 'orange']
print(arr_fruits)

for fruit in arr_fruits:
    print(str(arr_fruits.index(fruit)) + ' ' + fruit)

#filtration
even_nums = []
for num in range(1,30):
    if num % 2 == 0:
        even_nums.append(num)
print(even_nums)

#neighbors
data = [1,5,2,9,3]
for num in data:
    if data.index(num) < len(data)-1:
        print('current num is ' + str(num) + ', next num is ' + str(data[data.index(num)+1]))
