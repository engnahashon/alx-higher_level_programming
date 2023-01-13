#!/usr/bin/python3
def square(num):
    return num**2


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(square, i)))
    return new_matrix
