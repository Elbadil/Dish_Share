#!/usr/bin/python3
"""Defining a class BaseModel the base of all models of our web app"""
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import uuid


Base = declarative_base()


class BaseModel():
    """BaseModel of Dish Share Models"""

    id = Column(String(60), unique=True, nullable=False,
                primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __str__(self):
        """string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates and saves object"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionay representation of an object"""
        dictionay = self.__dict__.copy()
        dictionay['__class__'] = self.__class__.__name__
        dictionay['created_at'] = self.created_at.isoformat()
        dictionay['updated_at'] = self.updated_at.isoformat()
        return dictionay
