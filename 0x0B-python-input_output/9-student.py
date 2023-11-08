#!/usr/bin/python3
"""This module defines a student"""


class Student:
    """The student class"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Initialize an empty dictionary to store the serialized data"""
        serialized_data = {}

        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serialized_data[key] = value

        return serialized_data
