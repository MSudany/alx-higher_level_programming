#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elements = 0
    try:
        while num_of_elements != x:
            print(f'{my_list[num_of_elements]}', end='')
            num_of_elements += 1
    except IndexError:
        None
    print()
    return num_of_elements
