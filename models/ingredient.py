#!/usr/bin/python3
"""Defining a class Engredient"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text


class Ingredient(BaseModel, Base):
    """Ingredient Model of the web app"""

    __tablename__ = "ingredients"

    recipe_id = Column(String(60), ForeignKey('recipes.id'), nullable=False)
    name = Column(String(128), nullable=False)
    usage = Column(Text, nullable=False)
