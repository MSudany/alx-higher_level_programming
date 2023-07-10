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
'''
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value
'''
