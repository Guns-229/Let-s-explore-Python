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


def check_add(session, table, value):
    val = session.query(table).filter_by(name=value).first()
    if not val:
        print("Creating in ", table, val)
        val = table(name=value)
        session.add(val)
        session.flush()
        session.commit()
    return val

if __name__ == "__main__":
    print("Lets work !!! ")
    engine = create_engine("sqlite:///teachers_lessons_v2.sqlite3")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    s = Session()

    t1 = check_add(s, Teacher, "Sharma Sir")

    t1.lessons = [
        check_add(s, Lesson, "Inorganic"),
        check_add(s, Lesson, "Multiplication"),
        check_add(s, Lesson, "Organic")
    ]

    mlt = s.query(Lesson).filter_by(name="Multiplication").first()
    t2 = check_add(s, Teacher, "GuptaSir")

    t2.lessons = [
        mlt,
        check_add(s, Lesson, "Subtraction"),
        check_add(s, Lesson, "Algebra")
    ]
    s.commit()
