import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
# Always use uselist=Fase in relationship for one-to-one relationship.

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    card_id = Column(Integer, ForeignKey('card.id'))
    card = relationship("Card", uselist=False, back_populates="user")
    #child = relationship("Card", backref=backref("user", uselist=False), uselist=False)


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    user = relationship("User", uselist=False, back_populates="card")
    # parent_id = Column(Integer, ForeignKey('parent.id'))
    # parentage = relationship("Parent", backref=backref("child", uselist=False))


DB_FILE = "idcard_122.sqlite3"

try:
    os.remove(DB_FILE)
except Exception as e:
    print(e)
engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

mycard = Card(number="007007", user=User(name="mayank"))
session.add(mycard)
session.flush()
session.commit()

try:
    # It will move the card form mayank to roshan
    new_user = User(name="roshan")
    new_user.card = mycard
    session.add(new_user)
except Exception as e:
    print("ERROR:", e)

session.flush()
session.commit()

session.close()
engine.dispose()
