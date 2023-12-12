#!/usr/bin/python3
"""Unittest for Instruction model attributes and methods"""

import unittest
from app.models import BaseModel, User, Recipe, Instruction
from datetime import datetime
from app import app, db
import os


if os.getenv('TESTS'):
    class Test_Instruction_Init(unittest.TestCase):
        """Tests for Instruction's Parent Classes and Attributes"""

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
        
        def test_instruction_parent_classes(self):
            """check Instruction's Parent classes"""
            self.assertTrue(issubclass(Instruction, BaseModel))
            self.assertTrue(issubclass(Instruction, db.Model))

        def test_instruction_attributes(self):
            """tests for the attributes of the model Instruction"""
            instruction = Instruction()
            self.assertTrue(hasattr(instruction, "id"))
            self.assertTrue(hasattr(instruction, "created_at"))
            self.assertTrue(hasattr(instruction, "updated_at"))
            self.assertTrue(hasattr(instruction, "recipe_id"))
            self.assertTrue(hasattr(instruction, "step"))
            self.assertTrue(hasattr(instruction, "text"))

        def test_instruction_attributes_initialized(self):
            """test for initializing a new Instruction"""
            user = User(username="testuser", email="test@example.com", password="testpassword")
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
            self.assertIsInstance(instruction.id, str)
            self.assertIsInstance(instruction.created_at, datetime)
            self.assertIsInstance(instruction.updated_at, datetime)
            self.assertEqual(instruction.text, "Test Instruction")
            self.assertEqual(instruction.step, 1)
            self.assertEqual(instruction.recipe_id, recipe.id)


if __name__ == "__main__":
    unittest.main()
