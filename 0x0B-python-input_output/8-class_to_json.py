#!/usr/bin/python3
"""This module"""


def class_to_json(obj):
    """function that returns the dictionary description
        with simple data structure
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object is not an instance of a class.")

    serialized_data = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value

    return serialized_data
