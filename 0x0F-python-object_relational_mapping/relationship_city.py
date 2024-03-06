#!/usr/bin/python3
"""contains the class definition of a City."""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """This is the City class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
