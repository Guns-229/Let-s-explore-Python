"""."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

import os

DB_FILE = "faqs.sqlite3"
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

Base = declarative_base()
engine = create_engine('sqlite:///' + DB_FILE, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Topics(Base):
    """."""

    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    questions = relationship("Question", back_populates="topics",
                             cascade="all, delete, delete-orphan")

    def __str__(self):
        """."""
        return self.name


class Question(Base):
    """."""

    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    topics_id = Column(Integer, ForeignKey('topics.id'))
    topics = relationship("Topics", back_populates="questions")
    choices = relationship("Choice", back_populates="questions")

    def __str__(self):
        """."""
        return self.question

    def get_questions(self, topics):
        """."""
        print(self.objects.filter(topics=topics))


class Choice(Base):
    """."""

    __tablename__ = "choice"
    question_id = Column(Integer, ForeignKey('questions.id'))
    choice_text = Column(String)
    correct = Column(Boolean, default=False)
    question = relationship("Question", back_populates="choices")

    def __str__(self):
        """."""
        return self.choice_text
