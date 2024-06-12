#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def hbtn_status(url):
    r = requests.get(url)

    print("Body response:")
    print(f"\t- type: {r.text.__class__}")
    print(f"\t- content: {r.text}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    hbtn_status(url)
