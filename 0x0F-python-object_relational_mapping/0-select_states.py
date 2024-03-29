#!/usr/bin/python3
"""This is a simple MySQLdb script that lists all states in table"""
import MySQLdb
import sys


def states():
    """This is a simple function that lists all states in a table"""
    i = sys.argv[1]
    j = sys.argv[2]
    k = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=i, passwd=j, db=k, port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    states()
