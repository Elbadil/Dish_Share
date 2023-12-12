#!/usr/bin/python3
"""Unittest for Ingredient Model attributes and methods"""

import unittest
from app.models import BaseModel, User, Recipe, Ingredient
from datetime import datetime
from app import app, db
import os


if os.getenv('TESTS'):
    class Test_Ingredient_Init(unittest.TestCase):
        """Tests for Ingredient's Parent Classes and Attributes"""

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
        
        def test_ingredient_parent_classes(self):
            """check Ingredient's Parent classes"""
            self.assertTrue(issubclass(Ingredient, BaseModel))
            self.assertTrue(issubclass(Ingredient, db.Model))
        
        def test_ingredient_attributes(self):
            """tests for the attributes of the model Ingredient"""
            ingredient = Ingredient()
            self.assertTrue(hasattr(ingredient, "id"))
            self.assertTrue(hasattr(ingredient, "created_at"))
            self.assertTrue(hasattr(ingredient, "updated_at"))
            self.assertTrue(hasattr(ingredient, "recipe_id"))
            self.assertTrue(hasattr(ingredient, "name"))
            self.assertTrue(hasattr(ingredient, "order"))

        def test_ingredient_attributes_initialized(self):
            """test for initializing a new Ingredient"""
            user = User(username="testuser", email="test@example.com", password="testpassword")
            db.session.add(user)
            db.session.commit()
            recipe = Recipe(title="Test Recipe", description="Test description", user_id=user.id)
            db.session.add(recipe)
            db.session.commit()
            self.assertIn(recipe, user.recipes)
            ingredient = Ingredient(name="Test Ingredient", order=1, recipe_id=recipe.id)
            db.session.add(ingredient)
            db.session.commit()
            self.assertIn(ingredient, recipe.ingredients)
            self.assertIsInstance(ingredient.id, str)
            self.assertIsInstance(ingredient.created_at, datetime)
            self.assertIsInstance(ingredient.updated_at, datetime)
            self.assertEqual(ingredient.name, "Test Ingredient")
            self.assertEqual(ingredient.order, 1)
            self.assertEqual(ingredient.recipe_id, recipe.id)


if __name__ == "__main__":
    unittest.main()
