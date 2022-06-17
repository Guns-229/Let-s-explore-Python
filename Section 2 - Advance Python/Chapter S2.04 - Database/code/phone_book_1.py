import sqlobject
from sqlobject.sqlite import builder
conn = builder()('sqlobject_demo_relationships.db')
 

class PhoneNumber(sqlobject.SQLObject):
    _connection = conn
    number = sqlobject.StringCol(length=14, unique=True)
    owner = sqlobject.ForeignKey('Person')
    lastCall = sqlobject.DateTimeCol(default=None)
 
 
class Person(sqlobject.SQLObject):
    _idName='personID'
    _connection = conn
    name = sqlobject.StringCol(length=255)
    #The SQLObject-defined name for the "owner" field of PhoneNumber
    #is "owner_id" since it's a reference to another table's primary
    #key.
    numbers = sqlobject.MultipleJoin('PhoneNumber', joinColumn='owner_id')
Person.createTable(ifNotExists=True)
PhoneNumber.createTable(ifNotExists=True)

users = [('mayank', 2342323), ('rahul', 234456456)]

for user  in users:
    person = Person(name=user[0])
    p = PhoneNumber(number="{}".format(user[1]), owner=person)

