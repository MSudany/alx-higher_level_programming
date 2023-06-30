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
    def position(self, value):
        '''setter function'''
        if (type(value) is not tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''evaluates the area'''
        return self.size ** 2

    def my_print(self):
        '''prints the square'''
        if self.size == 0:
            print()
        else:
            for i in range(0, self.position[1]):
                print('')
                for j in range(0, self.size):
                    print(' ' * self.position, end='')
                    print('#' * self.size)
