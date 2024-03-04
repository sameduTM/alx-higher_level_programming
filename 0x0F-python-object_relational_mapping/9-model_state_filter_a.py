#!/usr/bin/python3
"""script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine, text
from model_state import Base, State


def state():
    """This is the only function of the script"""
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from states where name LIKE '%a%'"))

    rows = result.fetchall()

    for row in rows:
        print(str(row.id) + ":", row.name)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state()
