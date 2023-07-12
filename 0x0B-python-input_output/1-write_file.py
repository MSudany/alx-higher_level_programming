#!/usr/bin/python3
'''py oop'''


def write_file(filename="", text=""):
    '''writes a string to text file'''
    with open(filename, "w+", encoding='utf-8') as myFile:
        return myFile.write(text)
