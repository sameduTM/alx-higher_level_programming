#!/usr/bin/python3
"""script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine, text


def state():
    """States function"""
    with engine.connect() as conn:
        t = text("select * from states where name=:st_name")
        results = conn.execute(t, {"st_name": sys.argv[4]})

    rows = results.fetchall()

    if (len(rows) != 0):
        print(rows[0].id)
    else:
        print("Not found")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state()
