#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)

    ses = Session(eng)

    for state in ses.query(State).order_by(State.id).all():
        for c in state.name:
            if c == 'a':
                ses.delete(state)
                break
    ses.commit()
    ses.close()
