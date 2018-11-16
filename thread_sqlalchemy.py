from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///:memory:')

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

session = Session()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


Bob = Person(name='Bob')

session.add(Bob)
session.commit()
