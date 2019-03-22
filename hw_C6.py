#!/usr/bin/python3

with open('rosalind_subs.txt', 'r') as file:
    dna=file.read()

dna=dna.split()
dna0=dna[0]
dna1=dna[1]

result=[]

for i in range(1, len(dna0)-len(dna1)):
    if dna0[i-1:i-1+len(dna1)]==dna1:
                result.append(str(i))
print(' '.join(result))
