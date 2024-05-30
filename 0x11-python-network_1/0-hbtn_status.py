#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen
# from urllib.parse import urlencode

url = "https://alx-intranet.hbtn.io/status"

with urlopen(url) as response:
    body = response.read()
    char_set = response.headers.get_content_charset()

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode(char_set))
