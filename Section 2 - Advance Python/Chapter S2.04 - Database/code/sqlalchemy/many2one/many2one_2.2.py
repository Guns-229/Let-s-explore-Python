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
**back_populates** - alternative form of backref specification.

cascade="all, delete, delete-orphan".
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
#    school = relationship("School", back_populates="students")


class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Students", backref="school",
                            cascade="all, delete-orphan")


DB_FILE = "many2one_2.2.sqlite3"

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

# DELETE the school
session.delete(mayank.school)
session.flush()
session.commit()

session.close()
engine.dispose()
