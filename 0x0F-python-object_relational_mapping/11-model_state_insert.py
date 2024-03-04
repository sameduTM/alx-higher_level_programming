#!/usr/bin/python3
"""script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine, text


def state():
    """This is the state function"""
    with engine.connect() as conn:
        conn.execute(text("insert into states (name) values ('Louisiana')"))
        conn.commit()

    with engine.connect() as conn2:
        results = conn2.execute(text("SELECT * FROM states"))

        rows = results.fetchall()

    for row in rows:
        r = row

    print(r.id)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    state()
