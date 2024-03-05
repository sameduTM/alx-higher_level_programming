#!/usr/bin/python3
"""Script that changes the name of a State object
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text


def state():
    """This is the only function of script"""
    # create a connection
    with engine.connect() as conn:
        # create a transaction
        trans = conn.begin()
        conn.execute(text("UPDATE states SET name='New Mexico' WHERE id=2"))

        trans.commit()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state()
