#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body of
the response.
"""
import requests
import sys


def post_email(url, email):
    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
