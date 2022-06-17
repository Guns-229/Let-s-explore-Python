import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    card_id = Column(Integer, ForeignKey('card.id'), unique=True)
    card = relationship("Card", uselist=False)


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    user = relationship("User", uselist=False)


DB_FILE = "idcard_2.sqlite3"

try:
    os.remove(DB_FILE)
except Exception as e:
    print(e)
engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

mycard = Card(number="101111101")
user=User(name="mayank johri")
user.card = mycard

session.add(user)
session.flush()
session.commit()

session.close()
engine.dispose()
