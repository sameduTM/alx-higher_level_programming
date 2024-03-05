#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine, MetaData, text
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker


def rel():
    """This is the relationship function"""
    Session = sessionmaker(bind=engine)
    session = Session()

    calif = State(name="California")
    san_f = City(name="San Francisco", state=calif)

    session.add(calif)
    session.commit()
    session.close()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    rel()
