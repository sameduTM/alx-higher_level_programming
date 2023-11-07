#!/usr/bin/python3
"""This is the module with one function"""


def append_write(filename="", text=""):
    """This is append_write function"""
    with open(filename, mode='a', encoding='UTF8') as f:
        return f.write(text)
