#Пользователь вводит ненулевые целые числа до тех пор, пока не введет ноль. Найдите количество четных чисел, которые он ввел.

count = 0
while True:
    number = int(input("Введите ненулевое число : "))
    if number == 0:
        break
    elif number % 2 == 0:
        count += 1



print(count)




