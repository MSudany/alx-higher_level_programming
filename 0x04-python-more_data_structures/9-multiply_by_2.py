#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied = {}
    for i, item in a_dictionary.items():
        multiplied[i] = item * 2

    return multiplied
