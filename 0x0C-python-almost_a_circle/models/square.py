#!/usr/bin/python3
'''py oop'''


import sys
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class that inherits from rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialization'''
        super().__init__(size, size, x, y)

    def __str__(self):
        '''overloading Rectangle __str__ method'''
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute of a specific instance'''
        if args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        if not args and kwargs is not None:
            try:
                self.id = kwargs['id']
            except KeyError:
                pass
            try:
                self.width = kwargs['size']
                self.height = kwargs['size']
            except KeyError:
                pass
            try:
                self.x = kwargs['x']
            except KeyError:
                pass
            try:
                self.y = kwargs['y']
            except KeyError:
                pass
