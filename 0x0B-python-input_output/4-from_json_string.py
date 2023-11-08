#!/usr/bin/python3
"""This is ``from json to object`` module"""


def from_json_string(my_str):
    import json
    """from_json_string to obj function"""
    return json.loads(my_str)
