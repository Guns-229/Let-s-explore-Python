# -*- coding: utf-8 -*-
"""
Created on 30 Apr 2017
@author: Mayank Johri
Description:

In the below example we will be create a sample
for Many to one relationship using sqlalchemy
and then use back_populates feature

Tip:
-----
- backref: Add it two one relationship and another is not
           needed anymore.
"""


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
    # school = relationship("School", backref="students")


class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Students", backref="school",
                            cascade="all,delete,delete-orphan")


DB_FILE = "many2one_3_3.sqlite3"

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
# session.flush()

# session.commit()
mayank = Students(name="Mayank Johri")
mayank.school = dms
session.add(mayank)
session.add(Students(name="Anuja Johri", school=dms))
session.flush()

session.commit()

students = [
    "Sachin Shah",
    "Satendra",
    "Rajeev Chaturvedi"]

session.add_all([Students(name=student, school=dms) for student in students])
session.flush()
session.commit()

# --------------------------------------------------
cdac_students = [
    "Manish Gupta",
    "Viral Kamdar",
    "Pinakin Purohit",
    "Nitin Srivastava"]

cdac = session.query(School).filter_by(name="CDAC").first()

session.add_all([Students(name=student, school=cdac)
                 for student in cdac_students])
session.flush()
session.commit()
# # --------------------------------------------------
session.delete(mayank.school)
session.flush()
session.commit()
"""
Querying
-----------------------------------------------------------------------
A Query object is created using the query() method on Session.
It takes a number of arguments, which can be any combination of classes
and class-instrumented descriptors.
Below, we indicate a Query which loads Students instances.
When evaluated in an iterative context, the list of students
objects present is returned.
-----------------------------------------------------------------------
"""
print("*" * 20)
for student in session.query(Students).order_by(Students.id):
    print("{user} studied in {school}, {student}".format(user=student.name,
                                                         school=student.school.name,
                                                         student=student))
print("*" * 20)
for result in session.query(Students.name).order_by(Students.id):
    print("{user} was a student. {result}".format(user=result.name, result=result))
print("*" * 20)
for result in session.query(Students.name, Students.id).order_by(Students.id):
    print("{user} was a student. {id}".format(user=result.name, id=result.id))
print("*" * 20)
session.close()
engine.dispose()
