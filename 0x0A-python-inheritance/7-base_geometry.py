#!/usr/bin/python3
'''python oop'''


class BaseGeometry:
    '''class with 1 method'''
    def area(self):
        '''area method (not implemented yet)'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value (value is an int and greater than 1)'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
