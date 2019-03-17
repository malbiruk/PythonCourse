#!/usr/bin/python3
import math

print('Мы будем решать уравнение вида ax^2 + bx + c = 0')

abc=input('Введите через пробелы числа a b c: ')
abc=abc.split()

a=float(abc[0])
b=float(abc[1])
c=float(abc[2])

D=b**2-4*a*c

if D < 0:
    print('Корней нет.')

if D == 0:
    x=b*(-1)/(2*a)
    print(f'x = {x}')

if D > 0:
    x1=(b*(-1)+D**(1/2))/(2*a)
    x2=(b*(-1)-D**(1/2))/(2*a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
