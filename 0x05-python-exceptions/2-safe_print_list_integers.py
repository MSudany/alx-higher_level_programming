#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    real = 0
    try:
        while count != x:
            try:
                print('{:d}'.format(my_list[count]))
                count += 1
                real += 1
            except:
                count += 1
                continue
    except:
        None
    print()
    return real

