
# Object Relational Mapper using SQLAlchemy
---
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

## SQLALCHEMY'S PHILOSOPHY

SQL databases behave less like object collections the more size and performance start to matter; object collections behave less like tables and rows the more abstraction starts to matter. SQLAlchemy aims to accommodate both of these principles.

SQLAlchemy considers the database to be a relational algebra engine, not just a collection of tables. Rows can be selected from not only tables but also joins and other select statements; any of these units can be composed into a larger structure. SQLAlchemy's expression language builds on this concept from its core.

SQLAlchemy is most famous for its object-relational mapper (ORM), an optional component that provides the data mapper pattern, where classes can be mapped to the database in open ended, multiple ways - allowing the object model and database schema to develop in a cleanly decoupled way from the beginning.

SQLAlchemy's overall approach to these problems is entirely different from that of most other SQL / ORM tools, rooted in a so-called complimentarity- oriented approach; instead of hiding away SQL and object relational details behind a wall of automation, all processes are fully exposed within a series of composable, transparent tools. The library takes on the job of automating redundant tasks while the developer remains in control of how the database is organized and how SQL is constructed.


## SQLAlchemy Object Relational Mapper
----
The SQLAlchemy Object Relational Mapper presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables. It includes a system that transparently synchronizes all changes in state between objects and their related rows, called a unit of work, as well as a system for expressing database queries in terms of the user defined classes and their defined relationships between each other.

The ORM is in contrast to the SQLAlchemy Expression Language, upon which the ORM is constructed. Whereas the SQL Expression Language, introduced in SQL Expression Language Tutorial, presents a system of representing the primitive constructs of the relational database directly without opinion, the ORM presents a high level and abstracted pattern of usage, which itself is an example of applied usage of the Expression Language.

While there is overlap among the usage patterns of the ORM and the Expression Language, the similarities are more superficial than they may at first appear. One approaches the structure and content of data from the perspective of a user-defined domain model which is transparently persisted and refreshed from its underlying storage model. The other approaches it from the perspective of literal schema and SQL expression representations which are explicitly composed into messages consumed individually by the database.

A successful application may be constructed using the Object Relational Mapper exclusively. In advanced situations, an application constructed with the ORM may make occasional usage of the Expression Language directly in certain areas where specific database interactions are required.


```python
import sqlalchemy
print(sqlalchemy.__version__)
```

    1.0.12
    

### Python's SQLAlchemy and Declarative

There are three most important components in writing SQLAlchemy code:

* A Table that represents a table in a database.
* A mapper that maps a Python class to a table in a database.
* A class object that defines how a database record maps to a normal Python object.

Instead of having to write code for Table, mapper and the class object at different places, SQLAlchemy's declarative allows a Table, a mapper and a class object to be defined at once in one class definition.

## Connecting


```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
```

we will use an in-memory-only SQLite database. To connect we use create_engine():

The echo flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s standard logging module. With it enabled, we’ll see all the generated SQL produced. If you are working through this tutorial and want less output generated, set it to False. This tutorial will format the SQL behind a popup window so it doesn’t get in our way; just click the “SQL” links to see what’s being generated.

The return value of `create_engine()` is an instance of Engine, and it represents the core interface to the database, adapted through a dialect that handles the details of the database and DBAPI in use. In this case the SQLite dialect will interpret instructions to the Python built-in sqlite3 module.

The first time a method like `engine.execute()` or `engine.connect()` is called, the `engine` establishes a real DBAPI connection to the database, which is then used to emit the SQL. When using the ORM, we typically don’t use the `engine` directly once created; instead, it’s used behind the scenes by the ORM as we’ll see shortly.

> Lazy Connecting

> The `Engine`, when first returned by `create_engine()`, has not actually tried to connect to the database yet; that happens only the first time it is asked to perform a task against the database.


```python

```

## Declare a Mapping

When using the ORM, the configurational process starts by describing the database tables we’ll be dealing with, and then by defining our own classes which will be mapped to those tables. In modern SQLAlchemy, these two tasks are usually performed together, using a system known as Declarative, which allows us to create classes that include directives to describe the actual database table they will be mapped to.

Classes mapped using the Declarative system are defined in terms of a base class which maintains a catalog of classes and tables relative to that base - this is known as the declarative base class. Our application will usually have just one instance of this base in a commonly imported module. We create the base class using the declarative_base() function, as follows:


```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

Now that we have a “base”, we can define any number of mapped classes in terms of it. We will start with just a single table called users, which will store records for the end-users using our application. A new class called User will be the class to which we map this table. Within the class, we define details about the table to which we’ll be mapping, primarily the table name, and names and datatypes of columns:


```python
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
```

A class using Declarative at a minimum needs a \__tablename\__ attribute, and at least one Column which is part of a primary key [1]. SQLAlchemy never makes any assumptions by itself about the table to which a class refers, including that it has no built-in conventions for names, datatypes, or constraints. But this doesn’t mean boilerplate is required; instead, you’re encouraged to create your own automated conventions using helper functions and mixin classes, which is described in detail at Mixin and Custom Base Classes.

When our class is constructed, Declarative replaces all the Column objects with special Python accessors known as descriptors; this is a process known as instrumentation. The “instrumented” mapped class will provide us with the means to refer to our table in a SQL context as well as to persist and load the values of columns from the database.

Outside of what the mapping process does to our class, the class remains otherwise mostly a normal Python class, to which we can define any number of ordinary attributes and methods needed by our application.

## Create a Schema
With our User class constructed via the Declarative system, we have defined information about our table, known as table metadata. The object used by SQLAlchemy to represent this information for a specific table is called the Table object, and here Declarative has made one for us. We can see this object by inspecting the \__table\__ attribute:


```python
print(User.__table__)
```

    users
    


```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
        
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


if __name__ == "__main__":
    print(User.__table__)
    user = User("Mayank", "Mayank Johri", "password")
    print(user.fullname)
    print(user)
```

    users
    Mayank Johri
    <User(name='Mayank', fullname='Mayank Johri', password='password')>
    

## Creating a Session

The ORM’s “handle” to the database is the Session. When we first set up the application, at the same level as our `create_engine()` statement, we define a Session class which will serve as a factory for new Session objects:


```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

This custom-made Session class will create new Session objects which are bound to our database. Other transactional characteristics may be defined when calling `sessionmaker` as well; these are described in a later chapter. Then, whenever you need to have a conversation with the database, you instantiate a Session:


```python
session_dec = Session()
print(dir(session_dec))
```

    ['_Session__binds', '__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_bind', '_attach', '_autoflush', '_before_attach', '_bulk_save_mappings', '_close_impl', '_conditional_expire', '_connection_for_bind', '_contains_state', '_delete_impl', '_deleted', '_dirty_states', '_enable_transaction_accounting', '_expire_state', '_expunge_state', '_flush', '_flush_warning', '_flushing', '_identity_cls', '_is_clean', '_merge', '_new', '_query_cls', '_register_altered', '_register_newly_persistent', '_remove_newly_deleted', '_save_impl', '_save_or_update_impl', '_save_or_update_state', '_update_impl', '_validate_persistent', '_warn_on_events', 'add', 'add_all', 'autocommit', 'autoflush', 'begin', 'begin_nested', 'bind', 'bind_mapper', 'bind_table', 'bulk_insert_mappings', 'bulk_save_objects', 'bulk_update_mappings', 'close', 'close_all', 'commit', 'connection', 'connection_callable', 'delete', 'deleted', 'dirty', 'dispatch', 'enable_relationship_loading', 'execute', 'expire', 'expire_all', 'expire_on_commit', 'expunge', 'expunge_all', 'flush', 'get_bind', 'hash_key', 'identity_key', 'identity_map', 'info', 'invalidate', 'is_active', 'is_modified', 'merge', 'new', 'no_autoflush', 'object_session', 'prepare', 'prune', 'public_methods', 'query', 'refresh', 'rollback', 'scalar', 'transaction', 'twophase']
    

The above Session is associated with our SQLite-enabled Engine, but it hasn’t opened any connections yet. When it’s first used, it retrieves a connection from a pool of connections maintained by the Engine, and holds onto it until we commit all changes and/or close the session object.

## Use the Session
---
In this section you are going to insert, delete, update and query database objects using the session created in the previous section.

### Pre-requisites

### Insert

### Adding and Updating Objects

To persist our User object, we add() it to our Session:



```python
ed_user = User(name='Meenu', fullname='Meenakshi Johri', password='meenuInIndia')
session.add(ed_user)
```

> Check examples from 1 to 4


```python

```


```python

```


```python

```


```python


Import the session object from the object_test module:

>>> from object_test import session

Now import the model module and create a new page:

>>> import model

>>> test_page = model.Page()
>>> test_page.title = u'Test Page'
>>> test_page.content = u'Test content'
>>> test_page.title
u'Test Page'

Add the object to the session:

>>> session.add(test_page)
>>> print test_page.id
None

At this point the test_page object is known to SQLAlchemy, but not to the database. To send it to the database, a flush operation can be forced:

>>> session.flush()
>>> print test_page.id
1

Now let’s commit the changes:

>>> session.commit()

SQLAlchemy sends the COMMIT statement that permanently commits the flushed changes and ends the transaction.
Delete

To delete the test_page object from the database you would use:

>>> session.delete(test_page)
>>> session.flush()

At this point you can either commit the transaction or do a rollback. Let’s do a rollback this time:

>>> session.rollback()

SQLAlchemy sends a ROLLBACK statement to the database.
Query

Queries are performed with query objects that are created from the session. The simplest way to create and use a query object is like this:

>>> page_q = session.query(model.Page)
>>> for page in page_q:
...     print page.title
Test Page

Try the following statements and observe the SQL queries sent to the database by SQLAlchemy:

>>> page_q.all()

>>> page = page_q.first()
>>> page.title

>>> page_q[2:5]

>>> page_q.get(1)

Working with Objects

Now let’s think about how you could add a comment to a page. One approach would be to insert a new row in the comment table using the SQL Expression API, ensuring that the pageid field contained the value 1 so that the comment was associated with the correct page via a foreign key. The Object-Relational API provides a much better approach:

>>> comment1 = model.Comment()
>>> comment1.name= u'James'
>>> comment1.email = u'james@example.com'
>>> comment1.content = u'This page needs a bit more detail ;-)'
>>> comment2 = model.Comment()
>>> comment2.name = u'Mike'
>>> comment2.email = u'mike@example.com'
>>> page.comments.append(comment1)
>>> page.comments.append(comment2)
>>> session.commit()

The interesting thing to note is that rather than having manually set each comment’s .pageid attribute, you simply appended the comments to the page’s .comments attribute. Note also that there was no need to explicitely add the comments to the session, SQLAlchemy was smart enough to realize that they have been appended to an object that was already in the session.
```

### Other notable examples (Review in your free time)
Taken from http://www.programcreek.com/python/example/4713/sqlalchemy.create_engine 


```python
def setUp(self):
        self._engine = sqlalchemy.create_engine("sqlite:///:memory:")
        self._metadata = sqlalchemy.MetaData()
        self._metadata.bind = self._engine
        self._sports_table = sqlalchemy.Table("sports", self._metadata,
            sqlalchemy.Column("id_sports", sqlalchemy.Integer, primary_key=True),
            sqlalchemy.Column("name", sqlalchemy.String(100)),
            sqlalchemy.Column("weight", sqlalchemy.Float),
            sqlalchemy.Column("color", sqlalchemy.String(6)),
            sqlalchemy.Column("met", sqlalchemy.Float),
            sqlalchemy.Column("max_pace", sqlalchemy.Integer)
        )
        self._metadata.drop_all()
        self._metadata.create_all()
        
```


```python
def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = self._create_session()
        self._populate_database()
        self.query = self.session.query(User).order_by(asc(User.id))
        self.proxy = QueryResultProxy(self.query)
```


```python
def db_setup(test_subj, dbname=TEST_DB_NAME, dbdump=TEST_DB_DUMP, echo=False):
    """Sets up the db for use by a given test subject.

    test_subj must be an instance of DbTestFixture (or inheritated class),
    or the class itself. This allows using db_setup by
    - unittest setUp (instance method), or
    - unittest setUpClass (class method).

    """
    try:
        pg_createdb(dbname)
    except subprocess.CalledProcessError:  # try recovering once, in case
        pg_dropdb(dbname)			# the db already existed
        pg_createdb(dbname)
    test_subj.dbname = dbname
    test_subj.db = sqlalchemy.create_engine(
        'postgresql:///' + dbname, echo=echo)
    pg_restore(dbname, dbdump)
    Session = sqlalchemy.orm.sessionmaker()
    test_subj.session = Session(bind=test_subj.db)
```
