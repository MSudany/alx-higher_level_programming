#!/usr/bin/python3
'''python oop'''


def inherits_from(obj, a_class):
    '''tests if an obj is inherited directly or in-directly from a_class'''
    if (type(obj) is not a_class) and (isinstance(obj, a_class)):
        return True
    return False
