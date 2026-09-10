#if

# age = int(input("enter your age: "))
# if age <18:
#     print('you are young')
# elif age >= 18 and age <39:
#     print('you are adult')
# else:
#     print('you are old')

#calc discount
purchase_amount = 10000

if purchase_amount < 500:
    print('purchase amount less than 500')
    print('no discount')
elif purchase_amount > 500 and purchase_amount < 1000:
    print('purchase amount -', purchase_amount*0.95 )
elif purchase_amount > 1000 and purchase_amount < 5000:
    print('purchase amount -', purchase_amount*0.90 )
else:
    print('purchase amount -', purchase_amount*0.85 )

#while
index = 10
while index <= 10 and index >=0:
    print(index)
    index -= 1
print("START")

#for Summ of all number in range 100
total = 0
for x in range(101):
    total += x
print('total is ', total)

#for table of calculating 5
for x in range(1, 11):
    print( str(x) + ' * 5 = ' +str(int(x*5)))

#for + if
for x in range(1, 21):
    if x % 2 == 0:
        print( str(x) + ' четное ')
    elif x % 2 == 1:
        print(str(x) + ' не четное')

#while + if
secret_num = 9
bool_flag = True
while bool_flag:
   guess_num = int(input('please enter a number '))
   if guess_num == secret_num:
       print('you guessed the number')
       bool_flag = False
       break

#task with *
num = 29
for x in range(2,num):
    if num % x == 0:
        print(str(x) + ' - Составное')
        break
else:
    print('число простое ' + str(num))