from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import threading
import time

Base = declarative_base()
engine = create_engine('sqlite:///school.db')

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


def writing_thread():
    name_list = ['Christian', 'Mark', 'Bob', 'Will']

    for name in name_list:
        session = Session()
        person = Person(name=name)
        session.add(person)
        session.commit()
        time.sleep(1)


def reading_thread():
    for i in range(10):
        session = Session()
        e = session.query(Person).order_by(Person.id)[-1]
        print(e)
        time.sleep(1)
    Session.remove()


t1 = threading.Thread(target=writing_thread)
t2 = threading.Thread(target=reading_thread)

t1.start()
t2.start()
