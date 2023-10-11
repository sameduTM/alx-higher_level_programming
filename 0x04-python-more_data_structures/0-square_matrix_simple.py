#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res_mat = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res_mat[i][j] = matrix[i][j] ** 2

    return res_mat
