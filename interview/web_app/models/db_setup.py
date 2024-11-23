import os, datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


# defining tables as a python class
class Questions(Base):
    __tablename__ = 'questions'

    name = Column(String(80), nullable=False)
    descriptions = Column(String(3000), nullable=False)
    example = Column(String(3000))
    reference = Column(String(200))
    solved = Column(Boolean, default=False)
    added_time = Column(DateTime, default=datetime.datetime.now)
    last_solved = Column(DateTime, onupdate=datetime.datetime.now)
    id = Column(Integer, primary_key=True)


db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "quesions.db")
db_uri = 'sqlite:///{}'.format(db_dir)
engine = create_engine(db_uri)
Base.metadata.create_all(engine)
