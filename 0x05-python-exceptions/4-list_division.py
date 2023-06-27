#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    new_list = []
    while n < list_length:
        new = 0
        try:
            new = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            new = 0
            print('division by 0')
        except IndexError:
            new = 0
            print('out of range')
        except TypeError:
            print('wrong type')
        finally:
            new_list.append(new)
            n += 1
    return new_list
