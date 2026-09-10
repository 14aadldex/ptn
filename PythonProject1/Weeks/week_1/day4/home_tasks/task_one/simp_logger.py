from datetime import datetime

flag = True

with open('one_q.txt', 'a', newline='') as file:
    while flag:
        message = input("please enter a message for saving: ")
        now = datetime.now()
        file.write(str(now) + ' : ' + message + '\n')
        ask = input("continue? [y/n]")
        if ask == "n":
            flag = False
            break
