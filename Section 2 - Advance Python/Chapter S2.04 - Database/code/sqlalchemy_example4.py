# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 17:24:05 2016

@author: hclqaVirtualBox1
"""

#from history_meta import Versioned, /\versioned_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SomeClass( Base):
    __tablename__ = 'sometable'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __eq__(self, other):
        assert type(other) is SomeClass and other.id == self.id

dburl = 'sqlite:///test.db'
echo = True

engine = create_engine(dburl, echo=echo)
# Initialize database schema (create tables)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


sess = Session()
sc = SomeClass(name='sc1')
sess.add(sc)
sess.commit()

sc.name = 'sc1modified'
sess.commit()
