#!/usr/bin/python3

def prostnums(end):
    for i in range(2, end):
        if all(i % each != 0 for each in range(2, i-1)):
            yield i
