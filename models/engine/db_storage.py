#!/usr/bin/python3
"""Defining an engine class DBstorage"""
from models.base_model import BaseModel, Base
from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.comment import Comment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBstorage():
    """SQLAlchemy Engine class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes Engine"""
        user = getenv("DS_USER")
        pwd = getenv("DS_PWD")
        host = getenv("DS_HOST")
        db = getenv("DS_DB")
        link = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"

        self.__engine = create_engine(link, pool_pre_ping=True)