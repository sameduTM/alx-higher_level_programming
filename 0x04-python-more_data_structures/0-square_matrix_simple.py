#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res_matrix = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res_matrix[i][j] = matrix[i][j] ** 2

    return res_matrix
