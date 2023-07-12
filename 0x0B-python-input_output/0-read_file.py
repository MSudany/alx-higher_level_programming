#!/usr/bin/python3
'''py oop'''


def read_file(filename=""):
    '''opens a file, prints it to stdout'''
    with open(filename, encoding='utf-8') as myFile:
        for line in myFile:
            print(line)
