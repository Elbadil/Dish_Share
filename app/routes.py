#!/usr/bin/python3
"""Main routes for the web app"""
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from models.recipe import Recipe
from os import getenv
from dotenv import load_dotenv
import requests
import models

load_dotenv()

# Flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# recipe feed route
@app.route('/')
@app.route('/recipe_feed', strict_slashes=False)
def recipe_feed():
    """recipe feed page"""
    recipes = models.storage.all(Recipe)
    return render_template('feed.html', recipes=recipes, title='Recipe Feed')

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
