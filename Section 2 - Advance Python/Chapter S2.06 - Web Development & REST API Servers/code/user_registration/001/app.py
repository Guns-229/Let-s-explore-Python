#!/usr/bin/env python
# coding=utf-8
from flask import Flask, render_template, request
from flask import make_response
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.sql.expression import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/users.sqlite'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    questions = relationship("Questions", back_populates="topics")


@app.route("/regval", methods=['GET', 'POST'])
def register():
    """
    It requests for user details and then validate them,
    once validated, new valid user is added to db.
    """
    if request.method == 'POST':
        random_num = request.cookies.get("random_num")
        print(random_num)
        return render_template("validate.html",
                               result=request.form,
                               cookie=random_num)
    else:
        from uuid import uuid4
        resp = make_response(render_template('register.html'))
        resp.set_cookie('uuid', str(uuid4()))
        return resp


if __name__ == "__main__":
    app.run(debug=True)
