#!/usr/bin/python3
"""script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine, text
from model_state import Base, State


def state():
    """This is the only function of script"""
    with engine.connect() as conn:
        trans = conn.begin()

        conn.execute(text("DELETE FROM states WHERE (name) LIKE '%a%'"))
        trans.commit()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state()
