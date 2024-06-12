#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge.

-The first argument will be the repository name
-The second argument will be the owner name
-You must use the packages requests and sys
-You are not allowed to import packages other than requests and sys
-You dont need to check arguments passed to the script (number or type)
"""
import requests
import sys


def github_commits(repo, owner):
    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(owner, repo))
    cmt = r.json()
    i = 0
    while i < 10:
        print(f"{cmt[i]['sha']}: {cmt[i]['commit']['author']['name']}")
        i += 1


if __name__ == "__main__":
    github_commits(repo=sys.argv[1], owner=sys.argv[2])
