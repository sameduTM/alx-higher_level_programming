#!/usr/bin/python3
"""This is ``matrix division`` module"""


def matrix_divided(matrix, div):
    """This is the matrix division function"""
    x = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(
        isinstance(row, list)
        and all(isinstance(element, (int, float)) for element in row)
        for row in matrix
    ):
        raise TypeError(x)

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
