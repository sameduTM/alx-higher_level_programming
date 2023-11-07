#!/usr/bin/python3
"""This is the ``Read file`` module"""


def read_file(filename=""):
    """This is the read_file function"""
    with open(filename, encoding="UTF8") as f:
        print(f.read())
