#!/usr/bin/python3
"""Defining an engine class DBstorage"""
from models.base_model import Base, BaseModel
from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.comment import Comment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from os import getenv


load_dotenv()


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

    def all(self, cls=None):
        """Returns a dictionay of all objects of a class if defined
        else a dictionay of all objects"""
        dictionay = {}
        if cls is None:
            classes_to_query = [User, Recipe, Ingredient, Comment]
        else:
            if issubclass(cls, Base):
                classes_to_query = [cls]
            else:
                classes_to_query = []

        for clss in classes_to_query:
            objects = self.__session.query(clss).all()
            for obj in objects:
                if hasattr(obj, '_sa_instance_state'):
                    delattr(obj, '_sa_instance_state')
                dictionay[f'{obj.__class__.__name__}.{obj.id}'] = obj
  
        return dictionay

    def new(self, obj):
        """Adds the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Saves the changes to the database"""
        self.__session.commit()

    def delete(self, obj):
        """Deletes an object from database"""
        self.__session.delete(obj)

    def reload(self):
        """Reloads all database tables"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))    
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.close()

    def get(self, obj, obj_id):
        """Gets the object that matches the obj_id"""
        objts = self.__session.query(obj).all()
        if objts is None:
            return None
        else:
            for objt in objts:
                if objt.id == obj_id:
                    return objt
        return None
