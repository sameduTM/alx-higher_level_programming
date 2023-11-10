#!/usr/bin/python3
"""3. Same class or inherit from module"""


def is_kind_of_class(obj, a_class):
    """function checks f the object is an instance of,
    or if the object is an instance of a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
