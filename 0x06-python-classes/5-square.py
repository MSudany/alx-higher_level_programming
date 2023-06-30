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
        '''evaluates the area'''
        return self.__size ** 2

    def my_print(self):
        '''prints the square'''
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end='')
            print()
