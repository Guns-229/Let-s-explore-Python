from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


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


if __name__ == "__main__":

    engine = create_engine("sqlite:///user_keywords_v2.sqlite3")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    users = {}
    users['mayank'] = User('mayank')
    msi = Keyword('MSI Tester')
    users['mayank'].kw.append(msi)
    users['mayank'].kw.append(Keyword('WIX Tester'))
    users['mayank'].kw.append(Keyword('RPM Tester'))
    s.add_all(users.values())
    print(users['mayank'].kw)
    print(users['mayank'].kw[0].keyword)
    print([keyword.keyword for keyword in users['mayank'].kw])
    users['Aalok'] = User('Aalok')
    users['Aalok'].kw.append(msi)

    s.add_all(users.values())
    s.commit()
    print("---------------")
    print([keyword.keyword
           for tester in users.values()
           for keyword in tester.kw])
