#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """results = session.query(State).order_by(State.id).all()

    for row in results:
        print(f"{row.id}: {row.name}")
        for col in row.cities:
            print(f"    {col.id}: {col.name}")"""

    states_and_cities = (
        session.query(State)
        .join(City, State.id == City.state_id)
        .order_by(State.id, City.id).all()
    )

    for state in states_and_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
