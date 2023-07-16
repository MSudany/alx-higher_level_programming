#!/usr/bin/python3
'''py oop'''


import sys
import json
import os


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''JSON string representation of list_dictionaries'''
        if not list_dictionaries or list_dictionaries == '[]':
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        filename = '{}.json'.format(str(cls.__name__))
        new_list = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                new_list.append(list_objs[i].to_dictionary())
            json_str = cls.to_json_string(new_list)

        with open(filename, 'w') as myFile:
            myFile.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list from JSON string representation'''
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == 'Rectangle':
            dummy = cls(10, 10)
        else:
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = '{}.json'.format(cls.__name__)
        ls = []

        if os.path.exists(filename):
            with open(filename, 'r') as myFile:
                string = cls.from_json_string(myFile.read())
                for i in range(len(string)):
                    ls.append(cls.create(**string[i]))
        return ls
