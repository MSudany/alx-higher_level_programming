#!/usr/bin/python3
'''py oop'''


from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialization'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError('width must be int')
        if value < 1:
            raise ValueError('width must be > 1')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError('height must be int')
        if value < 1:
            raise ValueError('height must be > 1')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError('x must be int')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError('y must be int')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
