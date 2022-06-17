from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker as sm

Base = declarative_base()


def User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


engine = create_engine('sqlite://test.sqlite', echo=True)
Session = sm(bind=engine)





