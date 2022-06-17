# -*- coding: utf-8 -*-
"""
Created on 30 Apr 2017
@author: Mayank Johri
Description:

In the below example we will be create a sample
for Many to one relationship using sqlalchemy

Using backref: So only one relationship call needs to be make
and it will create the property on another object.

Tip:
-----
- Plase a foreign key in the parent table referencing the one.
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
    student = relationship("Students", backref="patshala")


DB_FILE = "one2many_basic_backref.sqlite"

try:
    os.remove(DB_FILE)
except Exception as e:
    print(e)

engine = create_engine('sqlite:///' + DB_FILE, echo=False)
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
print(dir(mayank))
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

#dms.student.append([Students(name=student, school=dms) for student in students])
#session.add(dms)
session.flush()
session.commit()
#
## --------------------------------------------------
cdac_students = [
    "Manish Gupta",
    "Viral Kamdar",
    "Pinakin Purohit",
    "Nitin Srivastava"]
#
## select * from school where name='CDAC' excluding first
cdac = session.query(School).filter_by(name="CDAC").first()
#
session.add_all([Students(name=student, patshala=cdac)
                 for student in cdac_students])
session.flush()
session.commit()
