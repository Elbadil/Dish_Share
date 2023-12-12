#!/usr/bin/python3
"""Unittest for Base_model Model attributes and methods"""

import unittest
from app.models import BaseModel, User, Recipe, Ingredient, Instruction, Comment
from datetime import datetime


class Test_BaseModel_Init(unittest.TestCase):
    """Tests for BaseModel's Subclasses and Attributes"""

    def test_subclass_BaseModel(self):
        """check BaseModel's subclasses"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(Recipe, BaseModel))
        self.assertTrue(issubclass(Ingredient, BaseModel))
        self.assertTrue(issubclass(Instruction, BaseModel))
        self.assertTrue(issubclass(Comment, BaseModel))


    def test_base_attributes(self):
        """tests for the attributes of the model BaseModel"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

class Test_BaseModel_Methods(unittest.TestCase):
    """Tests for BaseModel's Methods"""
    
    def test_repr_method(self):
        """test to the repr method of BaseModel"""
        base = BaseModel()
        base.id = "test_id"
        base.created_at = datetime(2023, 8, 11, 12, 0, 0)
        base.updated_at = datetime(2023, 8, 11, 12, 30, 0)
        expected_repr = (
            f"[BaseModel] (test_id) "
            f"{{'id': 'test_id', "
            f"'created_at': {repr(base.created_at)}, "
            f"'updated_at': {repr(base.updated_at)}}}"
        )
        self.assertEqual(repr(base), expected_repr)

    def test_update_method(self):
        """test to the update method of BaseModel"""
        base = BaseModel()
        base.id = "test_id"
        base.created_at = datetime(2023, 8, 11, 12, 0, 0)
        base.updated_at = datetime(2023, 8, 11, 12, 30, 0)
        before_update =  base.updated_at
        base.update()
        after_update = base.updated_at
        self.assertNotEqual(before_update, after_update)


if __name__ == "__main__":
    unittest.main()