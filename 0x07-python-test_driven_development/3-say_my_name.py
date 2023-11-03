#!/usr/bin/python3
"""
This is the ``say my name`` module

This module has only one function, say_my_name
"""


def say_my_name(first_name, last_name=""):
    """This is the say my name function"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        return None
    print(f"My name is {first_name} {last_name}")
