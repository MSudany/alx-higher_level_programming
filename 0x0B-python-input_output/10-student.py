#!/usr/bin/python3
'''py oop'''


class Student:
    '''defines a student'''

    def __init__(self, first_name, last_name, age):
        '''intiation'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''to json'''
        if attrs is not None
            return self.vars(attrs)
        return self.__dict__
