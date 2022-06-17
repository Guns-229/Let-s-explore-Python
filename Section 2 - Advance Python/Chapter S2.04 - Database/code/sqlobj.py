import sqlobject
from sqlobject.sqlite import builder
import random


conn = builder()('sqlobject_demo.db')


class PhoneNumber(sqlobject.SQLObject):
    _connection = conn
    number = sqlobject.StringCol(length=14, unique=True)
    owner = sqlobject.StringCol(length=255)
    lastCall = sqlobject.DateTimeCol(default=None)


PhoneNumber.createTable(ifNotExists=True)
myPhone = PhoneNumber(number='{}'.format(random.randint(40000000, 99999999)),
                      owner='Leonard Richardson')

try:
  # Running code with partial information will result in error
  duplicatePhone = PhoneNumber(number="(415) 555-1212")
except Exception as e:
  print(e)
