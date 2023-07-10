#!/usr/bin/python3
'''py oop'''


class MyList(list):
    '''class that inherits list'''

        def __init__(self):
            '''list initialization'''
            super().__init__()

        def print_sorted(self):
            '''prints a list that is sorted ascendingly'''
            print(sorted(self))
