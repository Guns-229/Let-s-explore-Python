#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:53:39 2018

@author: mayank
"""
from forms import SignupForm

from flask import Flask, request, render_template
from flask_login import LoginManager, login_user, login_required, logout_user


app = Flask(__name__)
app.secret_key = 'gMALVWEuxBSxQ44bomDOsWniejrPbhDV'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.sqlite'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return "Welcome to Home Page"


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if User.query.filter_by(email=form.email.data).first():
                return "!!! Email address already exists !!!"
            newuser = User(form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.flush()
            db.session.commit()
            login_user(newuser)
            return "User created!!!"
        else:
            return "Form didn't validate"


@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return "User logged in"
        return "<h1>Wrong username or password</h1>"

    return "form not validated or invalid request"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"


@app.route('/protected')
@login_required
def protected():
    return "protected area"


def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()


if __name__ == '__main__':
    from models import db, User
    init_db()
    app.run(port=5000, host='localhost')
