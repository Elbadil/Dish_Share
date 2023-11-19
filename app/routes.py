#!/usr/bin/python3
"""Main routes for the web app"""
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import requests

load_dotenv()

# recipe feed route
@app.route('/')
@app.route('/recipe_feed', strict_slashes=False)
def recipe_feed():
    """recipe feed page"""
    from app.models import Recipe
    recipes = Recipe.query.all()
    return render_template('feed.html', recipes=recipes, title="feed")

# Registration route
@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """Sign Up page"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('recipe_feed'))
    return render_template('register.html', form=form, title='Sign Up')

# Login route
@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login page"""
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'adel@blog.com' and form.password.data == 'adelelb':
            flash('You have been logged in', 'success')
            return redirect(url_for('recipe_feed'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', form=form, title='Login')


if __name__ == "__main__":
    app.run(debug=True)
