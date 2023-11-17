#!/usr/bin/python3
"""Defining a class Recipe"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Recipe(BaseModel, Base):
    """Recipe Model of the web app"""

    __tablename__ = "recipes"

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    title = Column(String(128), nullable=False)
    description = Column(Text, nullable=False)
    #image = Column(String(255), nullable=False)
    engredients = relationship('Ingredient', backref='recipe',
                               cascade='all, delete, delete-orphan')
