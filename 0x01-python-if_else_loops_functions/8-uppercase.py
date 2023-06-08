#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= 'a' and c <= 'z':
            c = c - 32
    print("{:s}".format(c), end='')
    print()
