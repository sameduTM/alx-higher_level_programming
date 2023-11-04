#!/usr/bin/python3
"""
This is the ``square`` module that prints a square

The module has only one function, print_square
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
