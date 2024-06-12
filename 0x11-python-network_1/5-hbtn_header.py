#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
import sys


def hbtn_header(url):
    r = requests.get(url)
    headers = r.headers
    print(headers['X-Request-Id'])


if __name__ == "__main__":
    url = sys.argv[1]
    hbtn_header(url)
