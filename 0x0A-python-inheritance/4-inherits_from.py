#!/usr/bin/python3
"""This is the ``Only sub class of`` module"""


def inherits_from(obj, a_class):
    """This is ``inherits from`` function"""
    if all(issubclass(type(obj), cls) for cls in a_class.mro()):
        return True
    else:
        return False
