#!/usr/bin/python3
"""Unittest for Recipe class attributes and methods"""

import unittest
from app.models import BaseModel, User, Recipe, Ingredient, Instruction
from datetime import datetime
from flask_login import UserMixin
from app import app, db
from sqlalchemy.exc import IntegrityError
import os


if os.getenv('TESTS'):
    class Test_Recipe_Init(unittest.TestCase):
        """Tests for Recipe's Parent Classes and Attributes"""

        @classmethod
        def setUpClass(cls):
            """Set Up the testing environment"""
            if os.getenv('TESTS'):
                cls.app = app  
                cls.app_context = cls.app.app_context()
                cls.app_context.push()
                db.create_all()

        @classmethod
        def tearDownClass(cls):
            """Tear down the testing environment"""
            if os.getenv('TESTS'):
                db.session.remove()
                db.drop_all()
                cls.app_context.pop()
        
        def test_recipe_parent_classes(self):
            """check Recipe's Parent classes"""
            self.assertTrue(issubclass(Recipe, BaseModel))
            self.assertTrue(issubclass(Recipe, db.Model))
    
        def test_recipe_attributes(self):
            """tests for the attributes of the model Recipe"""
            recipe = Recipe()
            self.assertTrue(hasattr(recipe, "id"))
            self.assertTrue(hasattr(recipe, "created_at"))
            self.assertTrue(hasattr(recipe, "updated_at"))
            self.assertTrue(hasattr(recipe, "user_id"))
            self.assertTrue(hasattr(recipe, "title"))
            self.assertTrue(hasattr(recipe, "image_file"))
            self.assertTrue(hasattr(recipe, "description"))
            self.assertTrue(hasattr(recipe, "ingredients"))
            self.assertTrue(hasattr(recipe, "instructions"))
        
        def test_recipe_attributes_initialized(self):
            """test for initializing a new Recipe"""
            user = User(username="testuser", email="test@example.com", password="testpassword")
            db.session.add(user)
            db.session.commit()
            recipe = Recipe(title="Test Recipe", description="Test description", user_id=user.id)
            db.session.add(recipe)
            db.session.commit()
            self.assertIsInstance(recipe.id, str)
            self.assertIsInstance(recipe.created_at, datetime)
            self.assertIsInstance(recipe.updated_at, datetime)
            self.assertEqual(recipe.title, "Test Recipe")
            self.assertEqual(recipe.description, "Test description")
            self.assertEqual(recipe.user_id, user.id)