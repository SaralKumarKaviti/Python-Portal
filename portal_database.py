import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base=declarative_base()

class Team(Base):
    __tablename__='team'
    id=Column(Integer,primary_key=True)
    name=Column(String(250),nullable=False)

class Tregister(Base):
    __tablename__='tregister'

    id=Column(Integer,primary_key=True)
    name=Column(String(250),nullable=False)
    tid=Column(String(50),nullable=False)
    tdate=Column(String(50),nullable=False)
    designation=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False)
    mobile=Column(String(50),nullable=False)
    photo=Column(String(50),nullable=False)
    trainer_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team)
    

engine = create_engine('sqlite:///pythonportal.db')

Base.metadata.create_all(engine)
