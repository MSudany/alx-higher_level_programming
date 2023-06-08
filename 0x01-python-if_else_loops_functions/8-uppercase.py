#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= 97 and c <= 122:
            c = c - 32
    print("{:c}".format(c), end='')
    print()
