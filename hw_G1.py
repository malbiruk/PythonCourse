#!/usr/bin/python3

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        name=func.__name__
        result = func(*args, **kwargs)
        with open('output.txt', 'w') as file:
            file.write(f'{name}: {result}')
        return result
    return wrapped
