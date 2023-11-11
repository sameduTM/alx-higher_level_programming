#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This is the ``Rectangle`` module"""


class Rectangle(BaseGeometry):
    """This is the child class Rectangle"""
    def __init__(self, width, height):
        """This is the only function of the class"""
        self.__width = width
        self.__height = height

        bg = BaseGeometry()
        bg.integer_validator("width", width)
        bg.integer_validator("height", height)
