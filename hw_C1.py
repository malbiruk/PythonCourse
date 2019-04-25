#!/usr/bin/python3

userlist = input('Введите числа (через пробелы): ')

userlist=userlist.split()

output=[]

for i in range(1, len(userlist)):
    if int(userlist[i]) > int(userlist[i-1]):
        output.append(userlist[i])

print (' '.join(output))
