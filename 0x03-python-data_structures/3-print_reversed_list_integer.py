#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return

    list.reverse(my_list)
    for i in my_list:
        print('{:d}'.format(i))
