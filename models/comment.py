#!/usr/bin/python3
"""Defining a class Comment"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text


class Comment(BaseModel, Base):
    """Comment Model for theweb app comments"""

    __tablename__ = "comments"

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    recipe_id = Column(String(60), ForeignKey('recipes.id'), nullable=False)
    recipe_comment = Column(Text)
