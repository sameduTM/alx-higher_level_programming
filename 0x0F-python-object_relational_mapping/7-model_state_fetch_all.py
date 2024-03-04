#!/usr/bin/python3
"""a script that lists all State objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, text


def state():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with engine.connect() as conn:
        result = conn.execute(text("select * from states order by id;"))

    rows = result.fetchall()

    for row in rows:
        print(str(row.id) + ":", row.name)


if __name__ == "__main__":
    state()
