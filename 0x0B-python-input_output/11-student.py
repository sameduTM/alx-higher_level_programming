#!/usr/bin/python3
"""This is the ``Student to disk and reload`` module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
             of a Student instance
        """
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

    def reload_from_json(self, json):
        """Update attributes based on the provided dictionary"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
