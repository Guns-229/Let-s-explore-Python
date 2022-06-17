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
    # no relation ship to students.
    # student = relationship("Students")


DB_FILE = "1_0_one2many_basic.sqlite"

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

session.add(School(name="CDAC, Hyderabad"))
session.flush()
session.commit()

mayank = Students(name="Mayank Johri")
mayank.school_id = dms.id
session.add(mayank)

session.commit()

students = session.query(Students).filter_by(school_id=1).all()
for student in students:
    print(student.name)

