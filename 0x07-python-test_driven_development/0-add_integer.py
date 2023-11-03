#!/usr/bin/python3
"""
This is the "addition" module

This module only has one function, add_integer
"""


def add_integer(a, b=98):
    """This is a simple addittion function"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
