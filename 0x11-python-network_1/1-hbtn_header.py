#!/usr/bin/python3
from urllib.request import urlopen
import sys

with urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
