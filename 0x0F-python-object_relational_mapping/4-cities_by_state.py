#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def state():
    """This is the only function in this script"""
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    state()
