#!/usr/bin/python3
"""This is the ``Only sub class of`` module"""


def inherits_from(obj, a_class):
    """This is ``inherits from`` function"""
    return any(issubclass(type(obj), cls) for cls in a_class.mro())
