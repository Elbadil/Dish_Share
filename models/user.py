#!/usr/bin/python3
"""Defining a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User Model for the web app users"""

    __tablename__ = "users"

    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    recipes = relationship('Recipe', backref='user',
                           cascade='all, delete, delete-orphan')
