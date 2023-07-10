#!/usr/bin/python3
'''py oop'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class that inherits Rectangle'''

    def __init__(self, size):
        '''Square initialization'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''returns square info'''
        return "[{}] {}/{}".format(type(self).__name__, self.__size,
                                   self.__size)
