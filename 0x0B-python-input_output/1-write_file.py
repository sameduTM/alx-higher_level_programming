#!/usr/bin/python3
"""This is the ``write to file`` module"""


def write_file(filename="", text=""):
    """This is the only write to file function in module"""
    with open(filename, mode="w", encoding="UTF8") as f:
        w = f.write(text)
        return w
