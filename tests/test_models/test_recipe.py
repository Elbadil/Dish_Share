#!/usr/bin/python3
"""Unittest for Recipe Model attributes and methods"""

import unittest
from app.models import BaseModel, User, Recipe, Ingredient, Instruction
from datetime import datetime
from app import app, db
import os


if os.getenv('TESTS'):
    class Test_Recipe_Init(unittest.TestCase):
        """Tests for Recipe's Parent Classes and Attributes"""

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
            self.assertIn(recipe, user.recipes)
            self.assertIsInstance(recipe.id, str)
            self.assertIsInstance(recipe.created_at, datetime)
            self.assertIsInstance(recipe.updated_at, datetime)
            self.assertEqual(recipe.title, "Test Recipe")
            self.assertEqual(recipe.description, "Test description")
            self.assertEqual(recipe.user_id, user.id)
        
        def test_recipe_ingredient_relationship(self):
            """test for recipe and Ingredient relationship"""
            user = User(username="testuser1", email="test1@example.com", password="testpassword")
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
        
        def test_recipe_instruction_relationship(self):
            """test for recipe and Instruction relationship"""
            user = User(username="testuser2", email="test2@example.com", password="testpassword")
            db.session.add(user)
            db.session.commit()
            recipe = Recipe(title="Test Recipe", description="Test description", user_id=user.id)
            db.session.add(recipe)
            db.session.commit()
            self.assertIn(recipe, user.recipes)
            instruction = Instruction(text="Test Instruction", step=1, recipe_id=recipe.id)
            db.session.add(instruction)
            db.session.commit()
            self.assertIn(instruction, recipe.instructions)


if __name__ == "__main__":
    unittest.main()
