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
    user = User("Mayank", "Mayank Johri", "password")
    print(user.fullname)
