#!/usr/bin/python3
"""Write a Python script that, displays the value of the X-Request-Id variable
"""
from urllib.request import urlopen
import sys

with urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
