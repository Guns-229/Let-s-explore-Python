"""
association_proxy:
associationproxy is used to create a read/write view of a target 
attribute across a relationship. It essentially conceals the usage 
of a “middle” attribute between two endpoints, and can be used to 
cherry-pick fields from a collection of related objects or to reduce 
the verbosity of using the association object pattern. 

Applied creatively, the association proxy allows the construction of 
sophisticated collections and dictionary views of virtually any geometry, 
persisted to the database using standard, transparently configured 
relational patterns.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    kw = relationship("Keyword", secondary=lambda: userkeywords_table)

    def __init__(self, name):
        self.name = name

    # proxy the 'keyword' attribute from the 'kw' relationship
    keywords = association_proxy('kw', 'keyword')


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
user.keywords.append(Keyword('MSI Tester'))
print(user.keywords[0].keyword)
user.keywords.append(Keyword('WIX Tester'))
user.keywords.append(Keyword('RPM Tester'))

print([Keywd.keyword for Keywd in user.keywords])
# The AssociationProxy object produced by the association_proxy()
# function is an instance of a Python descriptor. It is always
# declared with the user-defined class being mapped, regardless of
# whether Declarative or classical mappings via the mapper() function
# are used.

# The proxy functions by operating upon the underlying mapped
# attribute or collection in response to operations, and changes made
# via the proxy are immediately apparent in the mapped attribute, as
# well as vice versa. The underlying attribute remains fully
# accessible.

# When first accessed, the association proxy performs introspection
# operations on the target collection so that its behavior corresponds
# correctly. Details such as if the locally proxied attribute is a
# collection (as is typical) or a scalar reference, as well as if the
# collection acts like a set, list, or dictionary is taken into
# account, so that the proxy should act just like the underlying
# collection or attribute does.
