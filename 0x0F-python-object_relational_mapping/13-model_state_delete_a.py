#!/usr/bin/python3
"""
This script deletes all State objects with a name containing letter 'a'
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
