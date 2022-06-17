
# Databases
----
Following are the API's which can be used to access any database
## DB-API
---
The Python Database API (DB-API) defines a standard interface for Python database access modules. It’s documented in PEP 249. Nearly all Python database modules such as sqlite3, psycopg and mysql-python conform to this interface.
### Example


```python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 07:37:10 2016

@author: hclqaVirtualBox1
"""

try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite

DB_FILE = 'db/comment.sqlite3'
    
def createDB():
    import os
    
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)    
    db_conn = sqlite.connect(DB_FILE)
        
    db_curs = db_conn.cursor()
    db_curs.execute("""CREATE TABLE people (
                    id INTEGER PRIMARY KEY, first_name VARCHAR(20),
                    last_name VARCHAR(30), date_of_birth DATE)""")
    db_curs.execute("""INSERT INTO people (first_name, last_name, date_of_birth)
                         VALUES ('Mayank', 'Johri', '1976-7-10')""")
    db_curs.close()
    return db_conn

def getData(db_conn):
    db_cur = db_conn.cursor()
    sql = "select first_name, last_name, date_of_birth from people"
    db_cur.execute(sql)
    data = db_cur.fetchall()
    db_cur.close()
    return data

def getAllData(db_conn):
    db_cur = db_conn.cursor()
    sql = "select first_name, last_name, date_of_birth from people"
    db_cur.execute(sql)
    data = db_cur.fetchall()
    db_cur.close()
    return data
    

def setUser(db_conn, first_name, last_name, date_of_birth):
    stmt = """INSERT INTO people (first_name, 
                                  last_name, 
                                  date_of_birth) VALUES (?,?,?)"""
    db_cur = db_conn.cursor()
    db_cur.execute(stmt, (first_name, last_name, date_of_birth))
    
def rollback(db_conn):
    pass

def commit(db_conn):
    db_conn.commit()
    
if __name__ == "__main__":
    db_conn = None
    try:
      db_conn = createDB()
      setUser(db_conn, "Subhas", "Chandra Bose", "January 23, 1897")
      setUser(db_conn, "Bhagat", "Singh", "September 28, 1907")      
      data = getAllData(db_conn)
      print(type(data))
      for d in data:
          print("{0} {1} was born in {2}".format(d[0], d[1], d[2]))
    except:
      rollback(db_conn)
      raise 
    else:
      commit(db_conn)
    finally:
        if db_conn != None:
            db_conn.close()
```

    <class 'list'>
    Mayank Johri was born in 1976-7-10
    Subhas Chandra Bose was born in January 23, 1897
    Bhagat Singh was born in September 28, 1907
    


```python
try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite

DB_FILE = 'db/comment.sqlite3'


```

## SQLAlchemy
---
SQLAlchemy is a commonly used database toolkit. Unlike many database libraries it not only provides an ORM layer but also a generalized API for writing database-agnostic code without SQL.
> $ pip install sqlalchemy

### Example


```python

```

## Records

Records is minimalist SQL library, designed for sending raw SQL queries to various databases. Data can be used programmatically, or exported to a number of useful data formats.

> $ pip install records

Also included is a command-line tool for exporting SQL data.


```python

```

## SQLObject
--------
SQLObject is yet another ORM. It supports a wide variety of databases: Common database systems MySQL, Postgres and SQLite and more exotic systems like SAP DB, SyBase and MSSQL.


```python

```
