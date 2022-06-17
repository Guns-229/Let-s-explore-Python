# -*- coding: utf-8 -*-
"""
Created on 30 Apr 2017
@author: Mayank Johri
Description:

In the below example we will be create a sample
for Many to one relationship using sqlalchemy

Tip:
-----
- Place a foreign key in the parent table referencing the one.
- `relationship` is declared on the many, where a new scalar-holding
attribute will be created
- `Bidirectional` behavior can be achieved by
adding  relationship() in one and applying the
relationship.back_populates parameter in both directions """


# Common code starts(1)
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()
# Common code ends (1)


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    school_id = Column(Integer, ForeignKey('school.id'))


class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student = relationship("Students")


DB_FILE = "1_3_one2many_basic.sqlite"

try:
    os.remove(DB_FILE)
except Exception as e:
    print(e)

engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
dms = School()
dms.name = "Demonstration Multipurpose Higher Secondary School"
session.add(dms)

session.add(School(name="CDAC"))
session.flush()
session.commit()

mayank = Students(name="Mayank Johri")
dms.student.append(mayank)

dms.student.append(Students(name="Anuja Johri"))
session.add(dms)
session.flush()

session.commit()

students = [
    "Sachin Shah",
    "Satendra",
    "Rajeev Chaturvedi"]

for student in students:
    dms.student.append(Students(name=student))
session.commit()
#dms.student.append([Students(name=student, school=dms) for student in students])
#session.add(dms)
# session.flush()
# session.commit()
# #
# ## --------------------------------------------------
cdac_students = [
    "Manish Gupta",
    "Viral Kamdar",
    "Pinakin Purohit",
    "Nitin Srivastava"]
#
# ## select * from school where name='CDAC' excluding first
cdac = session.query(School).filter_by(name="CDAC").first()
# #

### Problem Problem Problem
session.add_all([Students(name=student, school=cdac)
                 for student in cdac_students])
session.flush()
session.commit()
# ## # --------------------------------------------------
# #print("^"*30)
# #print(session.dirty)
#
# #mayank.name = "mayank Johri"
#
# # """
# # session.dirty -
# # """
# ### HOW TO USE
# #print(session.dirty)
# #session.commit()
# #print(session.dirty)
# #print(help(session.dirty))
# #"""
# #Querying
# #-----------------------------------------------------------------------
# #A Query object is created using the query() method on Session.
# #It takes a number of arguments, which can be any combination of classes
# #and class-instrumented descriptors.
# #Below, we indicate a Query which loads Students instances.
# #When evaluated in an iterative context, the list of students
# #objects present is returned.
# #-----------------------------------------------------------------------
# #"""
# #print("*" * 20)
# #for student in session.query(Students).order_by(Students.id):
# #    print("{user} studied in {school}".format(user=student.name, school=student.school_id))
# #print("*" * 20)
# #for result in session.query(Students.name).order_by(Students.id):
# #    print("{user} was a student.".format(user=result.name))
# #
# #print("*" * 20)
# #for result in session.query(Students.name).order_by(Students.id):
# #    print("{user} was a student.".format(user=result.name))
# #
# #"""
# #ISSUES#
# ## --------------------------------------------------
# cdac_students = [
#     "Manish Gupta",
#     "Viral Kamdar",
#     "Pinakin Purohit",
#     "Nitin Srivastava"]
# #
# ## select * from school where name='CDAC' excluding first
# cdac = session.query(School).filter_by(name="CDAC").first()
# #
# session.add_all([Students(name=student, school=cdac)
#                  for student in cdac_students])
# #session.flush()
# #session.commit()
# ## # --------------------------------------------------
# #print("^"*30)
# #print(session.dirty)
#
# #mayank.name = "mayank Johri"
#
# # """
# # session.dirty -
# # """
# ### HOW TO USE
# #print(session.dirty)
# #session.commit()
# #print(session.dirty)
# #print(help(session.dirty))
# #"""
# #Querying
# #--------------------------------------
# #-----------------------------------------------------------------------
# #The issues with this topology is since its unidirectional in nature,
# #only through Students you can find their college name, but can not find
# #students from collage.
# #Also if we were to remove college then students will not be removed.
# #-----------------------------------------------------------------------
# #"""
# #print("*" * 20)
# #session.close()
# #engine.dispose()
