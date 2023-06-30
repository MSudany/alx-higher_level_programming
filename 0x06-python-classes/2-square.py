#!/usr/bin/python3
'''python oop'''


class Square():
    '''class of a square'''
    def __init__(self, size=0):
        '''class intialization
        
        Args:
            size (int): square size
        '''
        if (type(size) is not int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
