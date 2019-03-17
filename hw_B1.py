#!/usr/bin/python3
import sys
import operator

with open('rosalind_rna.txt', 'r') as file:
    dna=file.read()

print (dna.replace('T', 'U'))
