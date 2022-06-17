from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    kw = relationship("Keyword", secondary=lambda: userkeywords_table)

    def __init__(self, name):
        self.name = name


class Keyword(Base):
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    keyword = Column('keyword', String(64))

    def __init__(self, keyword):
        self.keyword = keyword


userkeywords_table = Table('userkeywords', Base.metadata,
                           Column('user_id', Integer,
                                  ForeignKey("user.id"),
                                  primary_key=True),
                           Column('keyword_id', Integer,
                                  ForeignKey("keyword.id"),
                                  primary_key=True))

user = User('mayank')
user.kw.append(Keyword('MSI Tester'))
user.kw.append(Keyword('WIX Tester'))
user.kw.append(Keyword('RPM Tester'))
print(user.kw)
print(user.kw[0].keyword)
print([keyword.keyword for keyword in user.kw])