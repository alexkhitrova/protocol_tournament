from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.db", echo=True)

Base = declarative_base()


class Teams(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    team_name = Column(String, unique=True)
    team_members = Column(String)
    grades = Column(String)
    max_grade = Column(Integer)
    tasks = Column(String, default="0 0 0 0 0 0 0 0 0")
    bonus_task = Column(Integer, default=-1)


Base.metadata.create_all(engine)  # sends CREATE TABLE
Session = sessionmaker(bind=engine)