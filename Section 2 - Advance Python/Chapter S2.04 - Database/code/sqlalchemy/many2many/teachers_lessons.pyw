from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

teachers_lessons = Table(
    "teachers_lessons",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
    Column("lesson_id", Integer, ForeignKey("lessons.id")),
)


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column("id", Integer, Sequence("teachers_id_seq"), primary_key=True)
    name = Column("name", String(50), nullable=False)

    lessons = relationship(
        "Lesson",
        backref="teachers",
        secondary=teachers_lessons
    )


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column("id", Integer, Sequence("lessons_id_seq"), primary_key=True)
    name = Column("name", String(50), nullable=False)


if __name__ == "__main__":
    print("Lets work !!! ")
    engine = create_engine("sqlite:///teachers_lessons.sqlite3")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    s = Session()

    t1 = Teacher(name="SharmaSir")
    t1.lessons = [
        Lesson(name="Inorganic"),
        Lesson(name="Multiplication"),
        Lesson(name="Organic")
    ]
    s.add(t1)
    t2 = Teacher(name="GuptaSir")
    t2.lessons = [
        Lesson(name="Multiplication"),
        Lesson(name="Subtraction"),
        Lesson(name="Algebra")
    ]
    s.add(t2)
    s.commit()
