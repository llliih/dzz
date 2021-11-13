#Даны катеты прямоугольного треугольника.
import math

cat1 = int(input("Введите длину катета 1:"))
cat2 = int(input("Введите длину катета 2:"))

#Найдите площадь, периметр и гипотенузу треугольника.
S = (cat1*cat2)/2
G = (cat1**2+cat2**2)
P = cat1+cat2+G
print(S)
print(math.sqrt(G))
print(P)