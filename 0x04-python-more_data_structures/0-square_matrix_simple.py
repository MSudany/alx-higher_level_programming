#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        sub_matrix = []
        for integer in i:
            sub_matrix.append(integer ** 2)
        square_matrix.append(sub_matrix)

    return square_matrix
