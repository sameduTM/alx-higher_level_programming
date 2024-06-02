#!/usr/bin/python3
from urllib.request import urlopen
import sys
import requests
"""Python script that displays the value of the X-Request-Id variable found in the header of the response.
"""

with urlopen(sys.argv[1]) as response:
    header = response.headers
    print(header['X-Request-Id'])
x = requests.Request.headers
