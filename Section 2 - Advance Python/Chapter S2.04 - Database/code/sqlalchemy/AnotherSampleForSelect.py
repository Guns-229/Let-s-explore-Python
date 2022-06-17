# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 06:08:38 2016

@author: Mayank Johri 
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)

import os

DB_FILE = "userinfo.sqlite3"
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)
session.add(User(name='ed', fullname='Ed Jones 1', password='edspassword 1'))
session.add(User(name='ed 2', fullname='Ed Jones 2', password='edspassword 2'))
session.add(User(name='test', fullname='Test User', password='TestUserspassword'))
session.flush()
session.commit()

our_user = session.query(User).filter_by(name='ed').first()

# for user in our_user:
#     print(user.fullname, user.name)


print("---------------")
print(ed_user is our_user)
print("---------------")

session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])

# Changing the Password for ed

ed_user.password = 'f8s7ccs'


"""
session.dirty -
"""
print(session.dirty)

# """
# session.new -
# """
# print(session.new)
#
session.commit()
print(session.dirty)
#
# """
# session.new -
# """
# print(session.new)
#
#
# """
# Querying
# --------------------------------
# A Query object is created using the query() method on Session. This function
# takes a variable number of arguments, which can be any combination of classes
# and class-instrumented descriptors. Below, we indicate a Query which loads
# User instances. When evaluated in an iterative context, the list of User
# objects present is returned:
# """
#
#
# for instance in session.query(User).order_by(User.id):
#     print(instance.name, instance.fullname)
#
#
for name, fullname in session.query(User.name, User.fullname):
    print(name, " is ", fullname)


for user in session.query(User).filter(User.name.in_(['ed', 'wendy', 'jack'])):
    print(user.fullname)

#
# """
# The tuples returned by Query are named tuples, supplied by the KeyedTuple
# class, and can be treated much like an ordinary Python object. The names are
# the same as the attribute’s name for an attribute,
# and the class name for a class:
# """
# for row in session.query(User, User.name).all():
#      print(row.User, row.name)
#
# for row in session.query(User.name.label('name_label')).all():
#     print(row.name_label)
#
# for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
#     print(name)
#
