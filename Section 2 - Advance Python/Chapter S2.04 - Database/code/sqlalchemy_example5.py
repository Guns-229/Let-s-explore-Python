from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

# engine.dispose()
engine = create_engine('sqlite:///userlist.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = 'address'

    address_id = Column(Integer, primary_key=True)
    house_name = Column(String)
    house_no = Column(String)
    city = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
ed_user = User(name='Meenu', fullname='Meenakshi Johri', password='meenuInIndia')
ad = Address(house_no="20", house_name="Raj Ghar", city= "Jaipur")
print(ed_user.id)
session.add(ed_user)
session.commit()
print(ed_user.id)
ad.user_id = ed_user.id

session.add(ad)

session.commit()
session.close()
engine.dispose()
