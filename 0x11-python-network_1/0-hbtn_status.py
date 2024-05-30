#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen
# from urllib.parse import urlencode

url = "https://alx-intranet.hbtn.io/status"

with urlopen(url) as response:
    body = response.read()
    char_set = response.headers.get_content_charset()

print("Body responses:")
print("- type:", type(body))
print("- content:", body)
print("- utf8 content:", body.decode(char_set))
