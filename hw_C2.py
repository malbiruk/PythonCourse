#!/usr/bin/python3

number=input('Введите натуральное число: ')

summ=0
mult=1

for i in range(len(number)):
    summ=summ+int(number[i])

for i in range(len(number)):
    mult=mult*int(number[i])

print(f'Сумма цифр: {summ}')
print(f'Произведение цифр: {mult}')
