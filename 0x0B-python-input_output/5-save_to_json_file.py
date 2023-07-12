#!/usr/bin/python3
'''py oop'''


import json


def save_to_json_file(my_obj, filename):
    '''writes my_obj to filename using a JSON string representation'''
    with open(filename, 'w', encoding='utf-8') as myFile:
        json.dump(my_obj, myFile)
