#!/usr/bin/python3
"""Defining Form for registration"""
from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    """Class for the registration Form"""
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Methode to validate users username"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken. Please choose a different one')

    def validate_email(self, email):
        """Methode to validate users email"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists. Please choose a different one')


class LoginForm(FlaskForm):
    """Class for the registration Form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """Class for the update account Form"""
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        """Methode to validate users username"""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is already taken. Please choose a different one')

    def validate_email(self, email):
        """Methode to validate users email"""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exists. Please choose a different one')


class Ingredients(Form):
    """For the Recipe Ingredients List of Fields"""
    ingredient = StringField(validators=[DataRequired()])


class Instructions(Form):
    """For the Recipe Instructions List of Fields"""
    instruction = TextAreaField(validators=[DataRequired()])


class PostForm(FlaskForm):
    """Class for the Post Recipe Form"""
    title = StringField('Recipe Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = FieldList(FormField(Ingredients), min_entries=3)
    instructions = FieldList(FormField(Instructions), min_entries=2)
    picture = FileField('Recipe Photo (optional)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Recipe')
