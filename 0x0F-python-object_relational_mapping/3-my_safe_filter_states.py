#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument,
one that is safe from MySQL injections!
"""
import MySQLdb
import sys


def state():
    """This is the only function of module"""
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306
                         )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY (%s)",
                (sys.argv[4], ))
    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    state()
