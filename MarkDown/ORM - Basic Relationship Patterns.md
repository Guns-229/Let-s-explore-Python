
# ORM - Basic Relationship Patterns
---



```python
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

## One To Many
----
A one to many relationship places a foreign key on the child table referencing the parent. `relationship()` is then specified on the parent, as referencing a collection of items represented by the child:


```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
```

To establish a bidirectional relationship in one-to-many, where the “reverse” side is a many to one, specify an additional `relationship()` and connect the two using the `relationship.back_populates` parameter:


```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")
```

`Child` will get a parent attribute with many-to-one semantics.

Alternatively, the `backref` option may be used on a single `relationship()` instead of using `back_populates`:


```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref="parent")
```

## Many To One
----
Many to one places a foreign key in the parent table referencing the child. relationship() is declared on the parent, where a new scalar-holding attribute will be created:


```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
```

Bidirectional behavior is achieved by adding a second relationship() and applying the relationship.back_populates parameter in both directions:


```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", back_populates="parents")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parents = relationship("Parent", back_populates="child")
```

Alternatively, the backref parameter may be applied to a single relationship(), such as Parent.child:



```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", backref="parents")
```

## One To One
---
One To One is essentially a bidirectional relationship with a scalar attribute on both sides. To achieve this, the uselist flag indicates the placement of a scalar attribute instead of a collection on the “many” side of the relationship. To convert one-to-many into one-to-one:


```python
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child = relationship("Child", uselist=False, back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="child")
```


```python
## Or for many-to-one:
----
As always, the relationship.backref and backref() functions may be used in lieu of the relationship.back_populates approach; to specify uselist on a backref, use the backref() function:
```


```python
from sqlalchemy.orm import backref

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", backref=backref("parent", uselist=False))
```

## Many To Many
----
Many to Many adds an association table between two classes. The association table is indicated by the secondary argument to relationship(). Usually, the Table uses the MetaData object associated with the declarative base class, so that the ForeignKey directives can locate the remote tables with which to link:



```python
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary=association_table)

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
```

For a bidirectional relationship, both sides of the relationship contain a collection. Specify using relationship.back_populates, and for each relationship() specify the common association table:



```python
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children")
```


```python
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary=association_table,
                    backref="parents")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
```


    ---------------------------------------------------------------------------

    InvalidRequestError                       Traceback (most recent call last)

    <ipython-input-4-128b0dd4e5f7> in <module>()
          1 association_table = Table('association', Base.metadata,
          2     Column('left_id', Integer, ForeignKey('left.id')),
    ----> 3     Column('right_id', Integer, ForeignKey('right.id'))
          4 )
          5 
    

    C:\apps\Anaconda3\lib\site-packages\sqlalchemy\sql\schema.py in __new__(cls, *args, **kw)
        396                     "to redefine "
        397                     "options and columns on an "
    --> 398                     "existing Table object." % key)
        399             table = metadata.tables[key]
        400             if extend_existing:
    

    InvalidRequestError: Table 'association' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.


The secondary argument of relationship() also accepts a callable that returns the ultimate argument, which is evaluated only when mappers are first used. Using this, we can define the association_table at a later point, as long as it’s available to the callable after all module initialization is complete:



```python
class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary=lambda: association_table,
                    backref="parents")
```

With the declarative extension in use, the traditional “string name of the table” is accepted as well, matching the name of the table as stored in Base.metadata.tables:



```python
class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary="association",
                    backref="parents")
```

## Deleting Rows from the Many to Many Table
----
A behavior which is unique to the secondary argument to relationship() is that the Table which is specified here is automatically subject to INSERT and DELETE statements, as objects are added or removed from the collection. There is no need to delete from this table manually. The act of removing a record from the collection will have the effect of the row being deleted on flush:



```python
# row will be deleted from the "secondary" table
# automatically
myparent.children.remove(somechild)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-c3a4c04f5e86> in <module>()
          1 # row will be deleted from the "secondary" table
          2 # automatically
    ----> 3 myparent.children.remove(somechild)
    

    NameError: name 'myparent' is not defined


A question which often arises is how the row in the “secondary” table can be deleted when the child object is handed directly to Session.delete():



```python
session.delete(somechild)
```


There are several possibilities here:

- If there is a relationship() from Parent to Child, but there is not a reverse-relationship that links a particular Child to each Parent, SQLAlchemy will not have any awareness that when deleting this particular Child object, it needs to maintain the “secondary” table that links it to the Parent. No delete of the “secondary” table will occur.
- If there is a relationship that links a particular Child to each Parent, suppose it’s called Child.parents, SQLAlchemy by default will load in the Child.parents collection to locate all Parent objects, and remove each row from the “secondary” table which establishes this link. Note that this relationship does not need to be bidrectional; SQLAlchemy is strictly looking at every relationship() associated with the Child object being deleted.
- A higher performing option here is to use ON DELETE CASCADE directives with the foreign keys used by the database. Assuming the database supports this feature, the database itself can be made to automatically delete rows in the “secondary” table as referencing rows in “child” are deleted. SQLAlchemy can be instructed to forego actively loading in the Child.parents collection in this case using the passive_deletes directive on relationship(); see Using Passive Deletes for more details on this.

Note again, these behaviors are only relevant to the secondary option used with relationship(). If dealing with association tables that are mapped explicitly and are not present in the secondary option of a relevant relationship(), cascade rules can be used instead to automatically delete entities in reaction to a related entity being deleted - see Cascades for information on this feature.



```python

```
