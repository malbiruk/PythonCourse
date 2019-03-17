#!/usr/bin/python3

string=input('Введите текст (без знаков препинания): ')
string=string.split()
lengths=[]

for i in string:
    lengths.append(len(i))

a=0
for place, number  in enumerate(lengths):
    if lengths[a] > number:
        a=place
print(f'Длина самого короткого слова: {lengths[a]}')
