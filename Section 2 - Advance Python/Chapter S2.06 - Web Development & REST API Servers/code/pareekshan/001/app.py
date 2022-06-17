#!/usr/bin/env python
# coding=utf-8
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/questions.sqlite'

db = SQLAlchemy(app)


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
    print(result, flush=True)
    return result


@app.route("/")
def home():
    topics = Topics.query.with_entities(Topics.name).all()
    topics = [r for r, in topics]
    print(topics)
    return render_template("index.html", topics=topics)


@app.route("/moolyaankan", methods=["POST"])
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
            # print(ch.correct, ch.id, sel, ch.correct and ch.id == int(sel))
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
def one_q():
    print(request.args)
    q_id = request.args.get("q_id")
    question = Questions.query.filter(Questions.id == q_id).first()

    return render_template("one_q.html", question=question)


@app.route("/start_quiz", methods=['GET'])
def start_quiz():
    no = 5
    topic_id = request.args.get('topic')
    print(topic_id)
    questions = Questions.query.order_by(
        func.random()).with_entities(Questions.id).filter(
        Questions.topics_id == topic_id).limit(no)
    print(questions)
    quest = [q[0] for q in questions]
    print(quest)
    return render_template("start_quiz.html", questions=quest)


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
    # print(get_topics())
