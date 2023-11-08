#!/usr/bin/python3
"""This is module defining a student"""


class Student:
    """This is the Student class"""
    def __init__(self, first_name, last_name, age):
        """This is the initialization instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This is a function to retrieve attributes"""
        if attrs is None:
            # If attrs is not provided, retrieve all attributes
            return self.__dict__
        else:
            # Initialize an empty dictionary to store the serialized data
            serialized_data = {}

            for attr in attrs:
                # Check if the attribute exists in the instance's dictionary
                if hasattr(self, attr):
                    serialized_data[attr] = getattr(self, attr)

            return serialized_data
