#!/usr/bin/env python
# coding=utf-8
from flask import Flask, render_template, request, url_for, redirect
from flask import session, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func
from werkzeug import secure_filename
import uuid
import os
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from utils import get_rand_string


app = Flask(__name__)
app.secret_key = get_rand_string(15, 20)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/questions.sqlite'
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password_hash = db.Column(db.String)
    filename = db.Column(db.String)

    def __init__(self, name=None, password=None, filename=None):
        if None not in [name, password, filename]:
            self.name = name
            self.password = password
            self.filename = filename

    def validate_password(self, _password):
        return check_password_hash(self.password_hash, _password)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


class Topics(db.Model):
    __tablename__ = "topics"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    questions = relationship("Questions", back_populates="topics")


class Questions(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    topics_id = db.Column(db.Integer, ForeignKey('topics.id'))
    topics = relationship("Topics", back_populates="questions")
    choices = relationship("Choice", back_populates="questions")


class Choice(db.Model):
    __tablename__ = "choice"
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, ForeignKey('questions.id'))
    questions = relationship("Questions", back_populates="choices")
    choice = db.Column(db.String)
    correct = db.Column(db.Boolean)


def get_topics():
    result = Topics.query.with_entities(Topics.name).all()
    result = [r for r, in result]
    print(result)
    return result


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not session.get('loggedIn', False):
            print("redirecting to login")
            return redirect(url_for("login"))
        print(session.get('loggedIn', False))
        return f(*args, **kwargs)
    return wrap


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        photo = request.files.get('user_photo', None)
        if None in [username, password, photo]:
            flash("Something is missing", "error")
            return render_template('register.html')
        ext = os.path.splitext(photo.filename)[1]
        new_filename = secure_filename(uuid.uuid4().hex + ext)
        photo.save(os.path.join("static/uploads/",
                                new_filename))
        user = Users.query.filter(
            Users.name == username).first()
        if user:
            flash("User already found", "error")
            return render_template('register.html')
        user = Users(username, password, new_filename)
        db.session.add(user)
        db.session.commit()
        flash('user registered successfully', "info")
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.route("/logout")
def logout():
    session['loggedIn'] = False
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        passwd = request.form.get('password', None)
        user = Users.query.filter(
            Users.name == username).first()
        if None in (username, passwd, user):
            flash('Invalid credentials !!!', 'error')
        elif not user.validate_password(passwd):
            flash('Invalid credentials', 'error')
        else:
            session.clear()
            print("Finally in else of login")
            session['loggedIn'] = True
            session['username'] = user.name
            response = make_response(redirect(url_for('home')))
            response.headers["authorization"] = user.name
            response.set_cookie('user', user.name)
            flash('Successfully logged in.', 'info')
            return response
    return render_template('login.html')


@login_required
@app.route("/")
def home():
    topics = Topics.query.with_entities(Topics.id, Topics.name).all()
    topic_details = [r for r in topics]
    return render_template("index.html",
                           topics=topic_details,
                           username=session['username'])


@app.route("/check_user", methods=["POST"])
def check_user():
    topic = request.form.get("topic")
    return redirect('/start_quiz?topic={topic}'.format(
                    topic=topic))


@app.route("/moolyaankan", methods=["POST"])
@login_required
def moolyaankan():
    print("moolyaankan")
    result = {
        "correct": 0,
        "wrong": 0
    }
    for quest, sel in request.form.items():
        # !!! Bad coding practice, will fix in later versions !!!
        # Lets validate if the selected answers are correct or not.
        question = Questions.query.filter(
            Questions.id == quest).first()
        print(question)
        got_it = False
        for ch in question.choices:
            if ch.correct and ch.id == int(sel):
                print("!!! Hurrey !!!")
                got_it = True
        if got_it:
            result["correct"] += 1
        else:
            result["wrong"] += 1
    return render_template("result.html", correct=result["correct"],
                           wrong=result["wrong"])


@app.route("/one_q", methods=['GET'])
@login_required
def one_q():
    print(request.args)
    q_id = request.args.get("q_id")
    question = Questions.query.filter(Questions.id == q_id).first()
    return render_template("one_q.html", question=question)


@app.route("/start_quiz", methods=['GET'])
@login_required
def start_quiz():
    no = 5
    topic_id = request.args.get('topic')
    questions = Questions.query.order_by(
        func.random()).with_entities(Questions.id).filter(
        Questions.topics_id == topic_id).limit(no)

    quest = [q[0] for q in questions]

    return render_template("start_quiz.html", questions=quest,
                           username=session['username'])


@login_required
@app.route("/show_result", methods=['POST'])
def show_result():
    selections = request.form
    correct_answers = 0
    for k, v in selections.items():
        if k.startswith("choice_"):
            print(Choice.query.filter(Choice.id == v).first().id)
            if Choice.query.filter(Choice.id == v).first().correct == 1:
                correct_answers += 1
            print(k, v)
    return "Thanks a lot:<br>Total correct Answers= " + str(correct_answers)


if __name__ == "__main__":
    app.run(debug=True)
