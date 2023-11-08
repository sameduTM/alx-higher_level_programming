#!/usr/bin/python3
"""This is a ``Save Object to a file`` module"""


def save_to_json_file(my_obj, filename):
    """This is the only function, save to json file"""
    import json
    with open(filename, mode='w', encoding='UTF8') as f:
        x = json.dumps(my_obj)
        return f.write(x)
