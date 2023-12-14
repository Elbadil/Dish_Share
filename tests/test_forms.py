#!/usr/bin/python3
"""Unittest for the Web App Forms"""

import unittest
from app.forms import RegistrationForm, LoginForm, PostForm, UpdateAccountForm
from app import app, db
import os


if os.getenv('TESTS'):
    class Test_Forms(unittest.TestCase):
        """Unit Tests for the Registration Form"""

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
        
        def test_registration_form_requirements(self):
            """Unit Tests for the Registration Form Requirements"""
            form = RegistrationForm()
            self.assertFalse(form.validate())
            self.assertIn('This field is required.', form.username.errors)
            self.assertIn('This field is required.', form.email.errors)
            self.assertIn('This field is required.', form.password.errors)
            self.assertIn('This field is required.', form.password_confirm.errors)
        
        def test_registration_form_validated(self):
            """Unit Tests for valid Registration Form """
            form_test = {
                "username": "testuser",
                "email": "test@example.com",
                "password": "testpassword",
                "password_confirm": "testpassword"
            }
            form = RegistrationForm(data=form_test)
            self.assertTrue(form.validate())
        
        def test_login_form_requirements(self):
            """Unit Tests for the Login Form Requirements"""
            form = LoginForm()
            self.assertFalse(form.validate())
            self.assertIn('This field is required.', form.email.errors)
            self.assertIn('This field is required.', form.password.errors)

        def test_login_form_validated(self):
            """Unit Tests for valid Login Form"""
            form_test = {"email": "test@example.com", "password": "testpassword"}
            form = LoginForm(data=form_test)
            self.assertTrue(form.validate())

        def test_UpdateAccount_form_requirements(self):
            """Unit Tests for the Login Form Requirements"""
            form = UpdateAccountForm()
            self.assertFalse(form.validate())
            self.assertIn('This field is required.', form.username.errors)
            self.assertIn('This field is required.', form.email.errors)

        def test_Post_form_requirements(self):
            """Unit Tests for the Post Form Requirements"""
            form = PostForm()
            self.assertFalse(form.validate())
            self.assertIn('This field is required.', form.title.errors)
            self.assertIn('This field is required.', form.description.errors)
            for entry in form.ingredients:
                self.assertIn('This field is required.', entry.ingredient.errors)
            for entry in form.instructions:
                self.assertIn('This field is required.', entry.instruction.errors)

        def test_Post_form_validated(self):
            """Unit Tests for valid the Post Form"""
            form_test = {
                "title": "test title",
                "description": "test description",
                "ingredients": [{"ingredient": "first"}, {"ingredient": "second"}],
                "instructions": [{"instruction": "first"}, {"instruction": "second"}],
            }
            form = PostForm(data=form_test)
            self.assertTrue(form.validate())


if __name__ == "__main__":
    unittest.main()
