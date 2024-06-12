#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]
r = requests.post(url, data={'q': q})

try:
    body = r.json()
    if len(body) > 0:
        print(f"[{body['id']}] {body['name']}")
    else:
        print("No result")
except TypeError:
    print("Not a valid JSON")
