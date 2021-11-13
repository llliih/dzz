y=int(input("введите число 0-камень, 1-ножницы, 2-бумага:"))#ваш выбор
if y == 1:
     print("ножницы")
elif y == 0:
     print("камень")
elif y == 2:
     print("бумага")
from random import randint
x=int(randint(0,2)) #выбор компьюера
if x == 1:
  print("ножницы")
elif x == 0:
     print("камень")
elif x == 2:
     print("бумага")
if y == 1 and x == 1:
          print("ничья")
elif y == 1 and x == 2:
          print('победа')
elif y == 1 and x == 0:
          print("проигрыш")
if y == 2 and x == 1:
          print("проигрыш")
elif y == 2 and x == 2:
          print('ничья')
elif y == 2 and x == 0:
          print("победа")
if y == 0 and x == 1:
          print("победа")
elif y == 0 and x == 2:
          print('проигрыш')
elif y == 0 and x == 0:
          print("ничья")
          





