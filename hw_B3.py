#!/usr/bin/python3

with open('rosalind_hamm.txt', 'r') as file:
    dna=file.read()

distance=0
dna_list=dna.split('\n')

dna0=dna_list[0]
dna1=dna_list[1]

for i in range(len(dna0)):
    if dna0[i] != dna1[i]:
        distance += 1

print(distance)
