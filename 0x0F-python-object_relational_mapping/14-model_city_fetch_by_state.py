#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)

    ses = Session(eng)
    for city, state in ses.query(City, State).\
            filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    ses.close()
