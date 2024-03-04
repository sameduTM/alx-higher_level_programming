#!/usr/bin/python3
"""a script that takes in the name of a state as an
argument and lists all cities of that state,
using the database"""
import MySQLdb
import sys


def city():
    """This is only function of module"""
    usrname = sys.argv[1]
    passwrd = sys.argv[2]
    dtbase = sys.argv[3]
    argc = sys.argv[4]
    db = MySQLdb.connect(host='localhost', user=usrname,
                         passwd=passwrd, db=dtbase, port=3306)
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities\
        INNER JOIN states ON\
        cities.state_id = states.id WHERE states.name = %s", (argc,))

    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))


if __name__ == '__main__':
    city()
