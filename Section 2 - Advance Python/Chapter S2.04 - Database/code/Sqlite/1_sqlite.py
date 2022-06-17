# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 07:37:10 2016

@author: mayank johri
"""

try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite

import os

DB_FILE = 'db/comment.sqlite3'

def createDB():
    try:
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
        db_conn = sqlite.connect(DB_FILE)

        db_curs = db_conn.cursor()
        db_curs.execute("""CREATE1 TABLE people (
                        id INTEGER PRIMARY KEY, first_name VARCHAR(20),
                        last_name VARCHAR(30), date_of_birth DATE)""")

        db_curs.execute("""INSERT INTO people (first_name, last_name, date_of_birth)
                             VALUES ('Mayank', 'Johri', '1976-7-10')""")
        db_curs.close()
    except:
        return None
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
    except:
        print("Sorry something went wrong in db connection")
    try:
        if db_conn != None:
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
