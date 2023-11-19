#!/usr/bin/python3
"""Main routes for the web app"""
from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user
from app.models import User
from app import app, db, bcrypt
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
        # Hashing the password of the user
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Adding the new user to the database
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"You're account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Sign Up')

# Login route
@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login page"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Setting up the user session after successful authentication
            login_user(user, remember=form.remember.data)
            return redirect(url_for('recipe_feed'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', form=form, title='Login')


if __name__ == "__main__":
    app.run(debug=True)
