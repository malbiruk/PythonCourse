#!/usr/bin/python3

with open('rosalind_revc.txt', 'r') as file:
    dna1=file.read()

dna2=list()

for i in dna1:
    letter = i
    if i == 'A':
        dna2.append('T')
    if i == 'T':
        dna2.append('A')
    if i == 'G':
        dna2.append('C')
    if i == 'C':
        dna2.append('G')

dna2_string=''.join(dna2)
print(f'{dna2_string[::-1]}')
