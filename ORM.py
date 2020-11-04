from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.db", echo=True)

Base = declarative_base()


class Teams(Base):
    __tablename__ = 'teams67'
    id = Column(Integer, primary_key=True)
    team_name = Column(String, unique=True)
    team_members = Column(String)
    grade = Column(Integer)
    t1 = Column(Integer)
    t2 = Column(Integer)
    t3 = Column(Integer)


Base.metadata.create_all(engine)  # sends CREATE TABLE
Session = sessionmaker(bind=engine)