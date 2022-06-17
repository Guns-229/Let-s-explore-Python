from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String
class City(Base):
    __tablename__ = 'City'

    id = Column(Integer, primary_key=True)
    DTCode = Column(String)
    DTName = Column(String)
    SDTCode = Column(String)
    SDTName = Column(String)
    TVCode = Column(String)
    Name = Column(String)