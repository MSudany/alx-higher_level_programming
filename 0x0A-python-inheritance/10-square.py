#!/usr/bin/python3
'''py oop'''


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    '''Square class that inherits Rectangle'''

    def __init__(self, size):
        '''Square initialization'''
        integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area():
        '''returns the area of the square'''
        return self.__size ** 2
