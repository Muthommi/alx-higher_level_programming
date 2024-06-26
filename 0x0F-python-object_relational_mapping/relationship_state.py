#!/usr/bin/python3
"""
This module defines the State class and Base instance for SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class inherits from Base and links to the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete, delete-orphan"
    )
