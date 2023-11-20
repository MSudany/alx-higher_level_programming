#!/usr/bin/python3
'''
...
'''


from sqlalchemy import create_engine
from sys import argv
from model_state import State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()

    state = session.query(State).order_by(State.id).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
