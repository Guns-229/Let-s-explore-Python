"""."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# import os

Base = declarative_base()


class DBSession():
    """."""

    def __init__(self, db_file="faqs.sqlite3"):
        """."""
        self.DB_FILE = db_file
        # if os.path.exists(self.DB_FILE):
        #     os.remove(self.DB_FILE)

        engine = create_engine('sqlite:///' + self.DB_FILE, echo=True)
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()


class Topics(Base):
    """."""

    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
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
    choices = relationship("Choice", back_populates="question")

    def __str__(self):
        """."""
        return self.question

    def get_questions(self, topics):
        """."""
        print(self.objects.filter(topics=topics))


class Choice(Base):
    """."""

    __tablename__ = "choice"
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    choice = Column(String)
    correct = Column(Boolean, default=False)
    question = relationship("Question", back_populates="choices")

    def __str__(self):
        """."""
        return self.choice
