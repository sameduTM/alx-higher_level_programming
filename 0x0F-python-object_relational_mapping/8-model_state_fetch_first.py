#!/usr/bin/python3
"""script that prints the first State object
from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, text


def state():
    """This is the only function in the module"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with engine.connect() as conn:
        result = conn.execute(text("select * from states order by states.id"))

    rows = result.fetchone()

    try:
        print(str(rows.id) + ":", rows.name)
    except AttributeError as e:
        print("Nothing")


if __name__ == "__main__":
    state()
