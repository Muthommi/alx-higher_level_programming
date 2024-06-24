#!/usr/bin/python3
"""A file that defines State class for the SQLAlchemy model."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class corresponding to the states table."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<state(id={self.id}, name='{self.name}')>"
