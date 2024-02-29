#!/usr/bin/python3
"""
    This is a simple MySQLdb script that lists all states in table
    in the database
"""

import MySQLdb
import sys

i = sys.argv[1]
j = sys.argv[2]
k = sys.argv[3]

db = MySQLdb.connect(host="localhost", user=i, passwd=j, db=k)

cur = db.cursor()
cur.execute("SELECT * FROM states")

rows = cur.fetchall()

for row in rows:
    print(row)
