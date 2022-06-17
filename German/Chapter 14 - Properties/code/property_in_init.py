import datetime

class STransaction(object):
    """A statement transaction"""
    def __init__(self, date):
        self._date = None
        self.date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        d = datetime.datetime.strptime(value, "%d-%b-%y")
        self._date = d


st = STransaction("20-Jan-10")
print(st.date)
