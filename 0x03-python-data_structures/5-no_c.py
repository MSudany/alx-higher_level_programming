#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    if my_string is None:
        return
    for c in my_string:
        if not(c =='c' or c =='C'):
            new_string.append(c)
    return ''.join(new_string)
