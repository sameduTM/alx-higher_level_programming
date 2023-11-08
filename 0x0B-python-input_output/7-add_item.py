#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file:"""


import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]

try:
    ex_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    ex_data = []

com_data = ex_data + args

save_to_json_file(com_data, 'add_item.json')
