#!/usr/bin/python3

with open('rosalind_hamm.txt', 'r') as file:
    dna=file.read()

distance=0
dna_list=dna.split('\n')



for i, letter1 in enumerate(dna_list[0]):
    for j, letter2 in enumerate(dna_list[1]):
        if i==j:
            if letter1 != letter2:
                distance += 1
print(distance)
