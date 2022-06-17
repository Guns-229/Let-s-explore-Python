# from flask import Flask, request
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
# from json import dumps
# 
# #Create a engine for connecting to SQLite3.
# #Assuming salaries.db is in your app root folder
# 
# e = create_engine('sqlite://db/cities.sqlite')
# 
# app = Flask(__name__)
# api = Api(app)
# 
# from sqlalchemy.ext.declarative import declarative_base
# 
# Base = declarative_base()
# from sqlalchemy import Column, Integer, String
# class City(Base):
#     __tablename__ = 'City'
# 
#     id = Column(Integer, primary_key=True)
#     DTCode = Column(String)
#     DTName = Column(String)
#     SDTCode = Column(String)
#     SDTName = Column(String)
#     TVCode = Column(String)
#     Name = Column(String)

import flask
import flask_sqlalchemy
import flask_restless

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/cities.sqlite'
db = flask_sqlalchemy.SQLAlchemy(app)

class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    STCode = db.Column(db.String)
    DTCode = db.Column(db.String)
    DTName = db.Column(db.String)
    SDTCode = db.Column(db.String)
    SDTName = db.Column(db.String)
    TVCode = db.Column(db.String)
    Name = db.Column(db.String)

# Create your Flask-SQLALchemy models as usual but with the following
# restriction: they must have an __init__ method that accepts keyword
# arguments for all columns (the constructor in
# flask_sqlalchemy.SQLAlchemy.Model supplies such a method, so you
# don't need to declare a new one).
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    birth_date = db.Column(db.Date)
# 
# 
# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Unicode)
#     published_at = db.Column(db.DateTime)
#     author_id = db.Column(db.Integer, db.ForeignKey('person.id'))
#     author = db.relationship(Person, backref=db.backref('articles',
#                                                         lazy='dynamic'))


# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(City, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Person, methods=['GET'])

# start the flask loop
app.run(debug=True)