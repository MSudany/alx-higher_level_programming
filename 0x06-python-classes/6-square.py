#!/usr/bin/python3
'''python oop'''


class Square():
    '''class of a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''instance intialization'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''retrive size'''
        return self.__size

    @property
    def position(self):
        '''retrive position'''
        return self.__position

    @size.setter
    def size(self, value):
        '''setter function'''
        if (type(value) is not int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def size(self, value):
        '''setter function'''
        if (type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position

    def area(self):
        '''evaluates the area'''
        return self.__size ** 2

    def my_print(self):
        '''prints the square'''
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print()
            for j in range(0, self.__size):
                print(self.__position * ' ')
                print(self.__size * '#')
