#!/usr/bin/python3
"""Unittest for User Model attributes and methods"""

import unittest
from app.models import BaseModel, User, Recipe
from datetime import datetime
from flask_login import UserMixin
from app import app, db
from sqlalchemy.exc import IntegrityError
import os


if os.getenv('TESTS'):
    class Test_User_Init(unittest.TestCase):
        """Tests for User's Parent Classes and Attributes"""

        @classmethod
        def setUpClass(cls):
            """Set Up the testing environment"""
            cls.app = app  
            cls.app_context = cls.app.app_context()
            cls.app_context.push()
            db.create_all()

        @classmethod
        def tearDownClass(cls):
            """Tear down the testing environment"""
            db.session.remove()
            db.drop_all()
            cls.app_context.pop()

        def test_user_parent_classes(self):
            """check User's Parent classes"""
            self.assertTrue(issubclass(User, BaseModel))
            self.assertTrue(issubclass(User, UserMixin))
            self.assertTrue(issubclass(User, db.Model))

        def test_user_attributes(self):
            """tests for the attributes of the model User"""
            user = User()
            self.assertTrue(hasattr(user, "id"))
            self.assertTrue(hasattr(user, "created_at"))
            self.assertTrue(hasattr(user, "updated_at"))
            self.assertTrue(hasattr(user, "username"))
            self.assertTrue(hasattr(user, "email"))
            self.assertTrue(hasattr(user, "image_file"))
            self.assertTrue(hasattr(user, "password"))
            self.assertTrue(hasattr(user, "recipes"))

        def test_user_attributes_initialized(self):
            """test for initializing a new User"""
            user = User(username="testuser", email="test@example.com", password="testpassword")
            db.session.add(user)
            db.session.commit()
            self.assertIsInstance(user.id, str)
            self.assertIsInstance(user.created_at, datetime)
            self.assertIsInstance(user.updated_at, datetime)
            self.assertEqual(user.username, "testuser")
            self.assertEqual(user.email, "test@example.com")
            self.assertEqual(user.image_file, "default.jpg")

        def test_user_unique_attributes(self):
            """test for unique attributes of User"""
            # Username
            user_1 = User(username="testuser1", email="test1@example.com", password="testpassword")
            db.session.add(user_1)
            db.session.commit()
            user_2 = User(username="testuser1", email="test2@example.com", password="testpassword")
            db.session.add(user_2)
            with self.assertRaises(IntegrityError):
                db.session.commit()
            db.session.rollback()

            # email
            user_3 = User(username="testuser3", email="test3@example.com", password="testpassword")
            db.session.add(user_3)
            db.session.commit()
            user_4 = User(username="testuser4", email="test3@example.com", password="testpassword")
            db.session.add(user_4)
            with self.assertRaises(IntegrityError):
                db.session.commit()
            db.session.rollback()
        
        def test_user_recipe_relationship(self):
            """test for user and recipe relationship"""
            user = User(username="test_user_recipe", email="test_user_recipe@example.com", password="testpassword")
            db.session.add(user)
            db.session.commit()
            recipe = Recipe(title="Test Recipe", description="Test description", user_id=user.id)
            db.session.add(recipe)
            db.session.commit()
            self.assertIn(recipe, user.recipes)



if __name__ == "__main__":
    unittest.main()
