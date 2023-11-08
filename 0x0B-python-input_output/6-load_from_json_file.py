#!/usr/bin/python3
"""This module creates Object from a ``JSON file``"""


def load_from_json_file(filename):
    """This is the only function"""
    import json
    with open(filename, encoding="UTF8") as f:
        return json.load(f)
