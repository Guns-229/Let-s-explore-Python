# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:07:26 2016

@author: hclqaVirtualBox1
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Comments(Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True)
    comment = Column(String)
    user_id = Column(Integer)


if __name__ == "__main__":
    engine = create_engine('sqlite:///userlist.sqlite3', echo=False)
    Base.metadata.create_all(engine)
    print("Tables created .....")
    Session = sessionmaker(bind=engine)
    session = Session()

    print(User.__table__)
    userinfo = [
        {"name": "Mayank 1", "fullname": "Mayank Johri", "password": "test@1234"},
        {"name": "Janki Mohan 1", "fullname": "Janki Mohan Johri", "password": "vinay@1234"},
        {"name": "Saroj 1", "fullname": "Saroj Johri", "password": "Saroj@1234"}
    ]

    for u in userinfo:
        user = User(name=u["name"], fullname=u["fullname"], password=u["password"])
        session.add(user)
        # session.commit()
    session.commit()
