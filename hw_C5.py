#!/usr/bin/python3

with open('rosalind_fib.txt', 'r') as file:
    nk=file.read()

nk=nk.split()
n=int(nk[0])
k=int(nk[1])

generations=[]

for i in range(n+1):
    if i < 2:
        generations.append(i)
    elif i == 2:
        generations.append(1)
    else:
        f=generations[i-1]+generations[i-2]*k
        generations.append(f)
print(generations[n])
