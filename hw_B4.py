#!/usr/bin/python3
import random


number=random.randint(1,100)

attempt1 = input('Угадайте число от 1 до 100: ')
attempt1=int(attempt1)

if attempt1 > number:
    print('Меньше')
elif attempt1 < number:
    print('Больше')
else:
    print('Верно!')

while True:
    attempt = input()
    attempt=int(attempt)
    if attempt > number:
        print('Меньше')
    elif attempt < number:
        print('Больше')
    else:
        print('Верно!')
        break
