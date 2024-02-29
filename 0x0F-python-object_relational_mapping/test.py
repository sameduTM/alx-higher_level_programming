#!/usr/bin/python3
import MySQLdb
import sys

"""
i = 'root'
j = 'root'
k = 'hbtn_0e_0_usa'
"""
i = sys.argv[1]
j = sys.argv[2]
k = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=i, passwd=j, db=k)

cur = db.cursor()
cur.execute("SELECT * FROM states")

rows = cur.fetchall()

for row in rows:
    print(row)