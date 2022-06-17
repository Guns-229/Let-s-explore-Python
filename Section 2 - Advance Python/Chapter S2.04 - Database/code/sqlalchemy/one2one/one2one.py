import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", 
                         backref=backref("parent", uselist=False), 
                         uselist=False)


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    # parent_id = Column(Integer, ForeignKey('parent.id'))
    # parentage = relationship("Parent", backref=backref("child", uselist=False))


DB_FILE = "one2one_2.1_temp.sqlite3"

try:
    os.remove(DB_FILE)
except Exception as e:
    print(e)
engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#oChild = session.query(Child).get(1)
#oParent = oChild.parent

# oParent2 = Parent()
# oParent.child = Child()


session.flush()
session.commit()

session.close()
engine.dispose()
