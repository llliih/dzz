#Робот может перемещаться в четырех направлениях («11» — север, «12» — запад, «13» — юг, «14» — восток) и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо.
x = int(input("Введите исходное положение от 11 до 14:"))#Дан число (11, 12, 13 или 14) — исходное направление робота
y = int(input("Введите исходное положение от -1 до 1:"))# и целое число N (0, 1 или -1) — посланная ему команда.
#Вывести направление робота после выполнения полученной команды (то есть север, запад, юг или восток).
if x + y == 11:
    print("север")
elif x + y == 10:
    print("восток")
elif x + y == 12:
    print("запад")
elif x + y == 13:
    print("юг")
elif x + y == 14:
    print("восток")
elif x + y == 15:
    print("север")
else:
    print("Не верное число")