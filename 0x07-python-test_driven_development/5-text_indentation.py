#!/usr/bin/python3
"""
This is the ''Text indentation'' module

This module has only one function, text_indentation
"""


def text_indentation(text):
    """This function prints 2 new lines after delimiter"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = len(text)
    i = 0
    while i < x:
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            if i == x:
                break
            print()
            print()
            i += 1
        i += 1
