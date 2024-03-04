#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa:
"""
import sys
from sqlalchemy import create_engine, text
from model_state import State, Base


def city():
    """This is city function"""
    with engine.connect() as conn:
        trans = conn.begin()
        results = conn.execute(text(
            "SELECT states.name, cities.id,\
            cities.name FROM states INNER JOIN cities ON\
                cities.state_id=states.id ORDER BY cities.id"))
    rows = results.fetchall()

    for row in rows:
        print(f"{row[0]}: ({row[1]}) {row[2]}")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    city()
