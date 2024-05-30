#!/usr/bin/python3
from urllib.request import urlopen
import sys
"""Python3 script that displays the value of the X-Request-Id variable found
in the header of the response.
"""

with urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
