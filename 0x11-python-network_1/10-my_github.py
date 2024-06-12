#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests


def my_github(user, passwd):
    r = requests.get('https://api.github.com/user', auth=(user, passwd))
    ghp = r.json()
    if r.status_code == 200:
        print(ghp['id'])
    else:
        print(None)


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    my_github(user, passwd)
