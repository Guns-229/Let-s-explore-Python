"""This is summary.

This is a basic module for getting
API Details to make the call
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class api_details(Base):
    """This is a class for api_details which will be used to create a db."""

    __tablename__ = 'api_details'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    api_type = Column(String)
    relative_url = Column(String)
    request_json = Column(String)

    def __init__(self, name, api_type, relative_url, request_json):
        """Initializer function."""
        self.name = name
        self.api_type = api_type
        self.relative_url = relative_url
        self.request_json = request_json

    def __repr__(self):
        """."""
        return """<APIDetails(name='%s',
                api_type='%s', relative_url='%s',
                request_json='%s')>""" % (self.name, self.api_type,
                                          self.relative_url, self.relative_url)
