#!/usr/bin/python3
'''python oop'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class (inherits from BaseGeometry)'''
    def __init__(self, width, height):
        '''initialization with width and height'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''returns rectangle object info'''
        return "[{}] {}/{}".format(type(self).__name__, self.__width,
                                   self.__height)
