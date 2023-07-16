#!/usr/bin/python3
'''py oop'''


from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialization'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        '''overriding __str__ method'''
        return '[{}] ({}) {:d}/{:d} - {:d}/{:d}'.format(self.__class__.__name__
                                                        , self.id,
                                                        self.x, self.y,
                                                        self.width, self.height
                                                        )

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the area'''
        return self.width * self.height

    def display(self):
        '''displays rectangle instance'''
        for i in range(self.height):
            for j in range(self.width):
                print('#', end='')
            print()
