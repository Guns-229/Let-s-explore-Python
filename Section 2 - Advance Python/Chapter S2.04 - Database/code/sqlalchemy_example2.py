# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:07:26 2016

@author: hclqaVirtualBox1
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


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


if __name__ == "__main__":
    print(User.__table__)
    userinfo = [
        {"name": "Mayank", "fullname": "Mayank Johri", "password": "test@1234"},
        {"name": "Janki Mohan", "fullname": "Janki Mohan Johri", "password" : "vinay@1234"},
        {"name": "Saroj", "fullname": "Saroj Johri", "password": "Saroj@1234"}
    ]

    users = []
    for u in userinfo:
        users.append(User(u["name"], u["fullname"], u["password"]))

    for user in users:
        if user.name == "Mayank" or user.password == "test@1234":
            print("HAHAHAH")
        print(user)
