#!/usr/bin/python3
"""This is the ``Rectangle`` module
    The module has two classes
"""


class BaseGeometry(object):
    """This is the ``Base geometry`` class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is the class Rectangle that inherits from Base Geometry"""
    def __init__(self, width, height):

        self.__width = width
        self.__height = height

        super().integer_validator("width", width)
        super().integer_validator("height", height)
