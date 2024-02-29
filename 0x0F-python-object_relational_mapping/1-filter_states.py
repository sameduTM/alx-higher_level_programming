#!/usr/bin/python3
"""This script lists all states with a name starting with N"""
import MySQLdb
import sys


def state():
    """This is the only function of module"""
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ")

    states = cur.fetchall()

    for i in states:
        print(i)


if __name__ == '__main__':
    state()
