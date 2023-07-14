#!/usr/bin/python3
'''py oop'''


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization'''
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
