#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def hbtn_status(url):
    r = requests.get(url)
    x = ' '
    print("Body response:")
    print(f"{4*x}- type: {r.text.__class__}")
    print(f"{4*x}- content: {r.text}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    hbtn_status(url)
