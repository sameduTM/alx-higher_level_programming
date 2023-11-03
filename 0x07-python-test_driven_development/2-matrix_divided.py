#!/usr/bin/python3
"""
This is the "matrix division" module

This module only has 1 function, matrix_divided
"""


def matrix_divided(matrix, div):
    """Function divides all elements of a matrix"""
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix.append(i / div)

    print(len(row))

    return new_matrix
