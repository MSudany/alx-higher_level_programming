#!/usr/bin/python3
'''python oop'''


class Square():
    '''class of a square'''
    def __init__(self, size=0):
        '''class intialization
        Args:
            size (int): square size
        '''
        self.__size = size

    @property
    def size(self):
        '''retrive size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter function'''
        if (type(value) is not int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''area function'''
        return self.__size ** 2
