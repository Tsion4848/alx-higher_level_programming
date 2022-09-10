#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import MySQLdb
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import update


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)

    ses = Session(eng)
    new = State(name="Louisiana")
    ses.add(new)
    ses.commit()
    for state in ses.query(State).filter_by(name="Louisiana")\
                                     .order_by(State.id).all():
        print("{}".format(state.id))
    ses.close()
