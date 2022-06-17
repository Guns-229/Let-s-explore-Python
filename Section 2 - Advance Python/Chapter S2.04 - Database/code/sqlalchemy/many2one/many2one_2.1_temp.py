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
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()
# Common code ends (1)


class Params(Base):
    __tablename__ = "params"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    value = Column(String)
    postData_id = Column(Integer, ForeignKey('postData.id'))


class PostData(Base):
    __tablename__ = "postData"
    id = Column(Integer, primary_key=True, unique=True)
    mimeType = Column(String)
    text = Column(String)
    params = relationship("Params",
                          backref="postData",
                          cascade="all,delete,delete-orphan")


DB_FILE = "many2one_2.1_temp.sqlite3"

try:
    os.remove(DB_FILE)
except Exception as e:
    print(e)
engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

post = PostData()


# request = Request()
# request.name = "TEST"
# request.headers.append(Headers(name="a", value="av"))
# request.headers.append(Headers(name="b", value="bv"))
# request.headers.append(Headers(name="c", value="cv"))
# request.headers.append(Headers(name="d", value="dv"))
# session.add(request)
# dms = School()
# dms.name = "Demonstration Multipurpose Higher Secondary School"
# session.add(dms)
# session.add(School(name="CDAC"))
# # session.flush()

# # session.commit()
# mayank = Students(name="Mayank Johri")
# mayank.school = dms
# session.add(mayank)
# session.add(Students(name="Anuja Johri", school=dms))
# session.flush()

# session.commit()

# students = [
    # "Sachin Shah",
    # "Satendra",
    # "Rajeev Chaturvedi"]

# session.add_all([Students(name=student, school=dms) for student in students])
# session.flush()
# session.commit()

# # --------------------------------------------------
# cdac_students = [
    # "Manish Gupta",
    # "Viral Kamdar",
    # "Pinakin Purohit",
    # "Nitin Srivastava"]

# cdac = session.query(School).filter_by(name="CDAC").first()

# session.add_all([Students(name=student, school=cdac)
                 # for student in cdac_students])
# session.flush()
# session.commit()
# # # --------------------------------------------------

# # DELETE the school
# session.delete(cdac)
session.flush()
session.commit()

session.close()
engine.dispose()
