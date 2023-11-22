#!/usr/bin/python3
"""Models for our web app"""
from app import db, login_manager
from datetime import datetime
from dotenv import load_dotenv
from flask_login import UserMixin
import uuid

load_dotenv()


@login_manager.user_loader
def load_user(user_id):
    """Returns the user that matches the given user_id"""
    return User.query.get(user_id)


class BaseModel:
    """Base model with common attributes."""
    id = db.Column(db.String(128), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def update(self):
        """Updated updated_at with the new datetime"""
        self.updated_at = datetime.utcnow()


class User(BaseModel, db.Model, UserMixin):
    """User Model for the web app users"""
    __tablename__ = "users"
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('Recipe',
                              backref='user', lazy=True, cascade='all, delete-orphan')


class Recipe(BaseModel, db.Model):
    """Recipe Model for the web app users recipes"""
    __tablename__ = "recipes"
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20))
    description = db.Column(db.Text, nullable=False)
    ingredients = db.relationship('Ingredient',
                                  backref='recipe', cascade='all, delete-orphan',
                                  lazy=True)
    instructions = db.relationship('Instruction',
                                  backref='recipe', cascade='all, delete-orphan',
                                  lazy=True)
    comments = db.relationship('Comment',
                               backref='recipe', cascade='all, delete-orphan',
                               lazy=True)


class Ingredient(BaseModel, db.Model):
    """Ingredient Model for the web app users recipes ingredients"""
    __tablename__ = "ingredients"
    recipe_id = db.Column(db.String(128), db.ForeignKey('recipes.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    order = db.Column(db.Integer, nullable=False)


class Instruction(BaseModel, db.Model):
    """Comment Model for the web app users recipes instructions"""
    __tablename__ = "instructions"
    recipe_id = db.Column(db.String(128), db.ForeignKey('recipes.id'), nullable=False)
    step = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)


class Comment(BaseModel, db.Model):
    """Comment Model for the web app recipes comments"""
    __tablename__ = "comments"
    recipe_id = db.Column(db.String(128), db.ForeignKey('recipes.id'), nullable=False)
    text = db.Column(db.Text)
