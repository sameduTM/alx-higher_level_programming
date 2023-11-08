#!/usr/bin/python3
"""Pascal's triangle module"""


def pascal_triangle(n):
    """This module only has one function, pascal_triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            # Calculate the next row based on the previous row
            previous_row = triangle[i - 1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(previous_row[j - 1] + previous_row[j])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
