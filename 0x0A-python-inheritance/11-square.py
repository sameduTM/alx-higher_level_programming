#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""This is the ``Square 2`` module"""


class Square(Rectangle):
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
