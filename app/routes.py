#!/usr/bin/python3
"""Main routes for the web app"""
from flask import render_template, url_for, flash, redirect, request, abort
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, Recipe, Ingredient, Instruction
from app import app, db, bcrypt
from PIL import Image
import secrets
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# Spooncular API
SPN_API = "https://api.spoonacular.com/recipes/complexSearch"
API_KEY = os.getenv('API_KEY')

# Home page route
@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """Search Recipes"""
    if request.method == 'POST':
        # If a form is submitted
        query = request.form.get('search_query', '')
        # Perform a search for recipes with the given query
        recipes = search_recipes(query)
        return render_template('search.html', title=query,
                                   recipes=recipes['results'],
                                   search_query=query)
    # If it's a get request or no form is submitted return to index route
    return render_template('index.html')


# Defining a function that searches for recipes based on query
def search_recipes(query):
    """Returns recipes based on a given query"""
    params = {'apiKey': API_KEY,
              'query': query,
              'addRecipeInformation': True,
              'number': 15}
    req = requests.get(SPN_API, params=params)
    if req.status_code == 200:
        recipes = req.json()
        return recipes
    return []


# Home page route
@app.route('/home', strict_slashes=False)
def home():
    """home page"""
    params = {'apiKey': API_KEY,
              'number': 12}
    req = requests.get(SPN_API, params=params)
    counter = 0
    first_four = []
    second_four = []
    third_four = []
    for recipe in req.json()['results']:
        if counter < 4:
            first_four.append(recipe)
        elif counter < 8:
            second_four.append(recipe)
        else:
            third_four.append(recipe)
        counter += 1

    return render_template('home.html', title="Home", first_four=first_four,
                           second_four=second_four, third_four=third_four)


# External Recipes routes
@app.route('/extern_recipes/<recipe_id>', strict_slashes=False)
def extern_recipe(recipe_id):
    """External Recipe page that matches the id given"""
    recipe_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {'apiKey': API_KEY}
    req = requests.get(recipe_url, params=params)
    if req.status_code == 200:
        recipe = req.json()
        return render_template('extern_recipe.html', recipe=recipe, title=recipe['title'])
    return "Recipe not found", 404


# Home dish page route
@app.route('/recipes/Spaghetti-alla-Carbonara', strict_slashes=False)
def main_dish():
    """Route for the main dish information"""
    return render_template('home_dish.html', title="Spaghetti alla Carbonara")


# About section route
@app.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """About section of the web app"""
    return render_template('about.html', title="About Us")


# recipe feed route
@app.route('/recipe_feed', strict_slashes=False)
def recipe_feed():
    """recipe feed page"""
    from app.models import Recipe
    page = request.args.get('page', 1, type=int)
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=5)
    return render_template('feed.html', recipes=recipes, title="Recipe Feed")


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
            # the page that the user was not allowed to enter
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'error')
    return render_template('login.html', form=form, title='Login')


# Logout route
@app.route('/logout', strict_slashes=False)
def logout():
    """Logout page"""
    logout_user()
    return redirect(url_for('index'))


# Saves the profile picture entered by the user and returns the path
def save_picture(form_picture):
    """Saves the profile picture of the user in the static/images directory
    and returs the picture's file path"""
    picture_extension = form_picture.filename.split('.')[1]
    random_hex = secrets.token_hex(8)
    picture_fn = random_hex + '.' + picture_extension
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    # Resize the picture before saving
    # output_size = (250, 250)
    # i = Image.open(form_picture)
    # i.thumbnail(output_size)
    # saves the picture to the specified file path using the save method
    form_picture.save(picture_path)
    # i.save(picture_path)
    return picture_fn


# account route
@app.route('/account', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def account():
    """User Profile Page"""
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.update()
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    # Displays the current email and username in the inputs
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename=f'images/{current_user.image_file}')
    return render_template('account.html', title=current_user.username,
                           image_file=image_file, form=form)


# Post new recipe route
@app.route('/recipe/new', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def new_recipe():
    """Adds new recipe by the user"""
    form = PostForm()
    if form.validate_on_submit():
        recipe = Recipe(user_id=current_user.id, title=form.title.data, description=form.description.data)
        if form.picture.data:
            picture_fn = save_picture(form.picture.data)
            recipe.image_file = picture_fn
        db.session.add(recipe)
        db.session.commit()
        # Add Recipe Ingredients
        order = 1
        for ingredient in form.ingredients:
            new_ingredient = Ingredient(recipe_id=recipe.id, name=ingredient.data['ingredient'], order=order)
            db.session.add(new_ingredient)
            order += 1
        # Add Recipe Instructions
        step = 1
        for instruction in form.instructions:
            new_instruction = Instruction(recipe_id=recipe.id, text=instruction.data['instruction'], step=step)
            db.session.add(new_instruction)
            step += 1
        db.session.commit()
        flash('Your new Recipe has been posted!', 'success')
        return redirect(url_for('recipe_feed'))
    return render_template('new_recipe.html', form=form, title="Add a Recipe")


# recipes routes based on recipe id
@app.route('/recipe/<recipe_id>', strict_slashes=False)
def recipe(recipe_id):
    """Recipe page based on its id"""
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', title=recipe.title, recipe=recipe)


# recipes update routes based on recipe id
@app.route('/recipe/<recipe_id>/update', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def update_recipe(recipe_id):
    """Updates a Recipe that matches the id given"""
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = []
        recipe.instructions = []
        # Update Recipe Ingredients
        order = 1
        for ingredient in form.ingredients:
            new_ingredient = Ingredient(recipe_id=recipe.id, name=ingredient.data['ingredient'], order=order)
            db.session.add(new_ingredient)
            order += 1
        # Update Recipe Instructions
        step = 1
        for instruction in form.instructions:
            new_instruction = Instruction(recipe_id=recipe.id, text=instruction.data['instruction'], step=step)
            db.session.add(new_instruction)
            step += 1
        if form.picture.data:
            picture_fn = save_picture(form.picture.data)
            recipe.image_file = picture_fn
        db.session.commit()
        flash('Recipe has been updated successfully!', 'success')
        return redirect(url_for('recipe', recipe_id=recipe.id))
    elif request.method == 'GET':
        form.title.data = recipe.title
        form.description.data = recipe.description
        form.ingredients.entries = []
        form.instructions.entries = []
        # Append new Ingredients entries based on existing data
        for _ in range(len(recipe.ingredients)):
            form.ingredients.append_entry()
        # Fill data for existing Ingredients entries
        for i, ingredient_entry in enumerate(form.ingredients.entries):
            ingredient_entry.form.ingredient.data = sorted(recipe.ingredients, key=lambda x: x.order)[i].name
        # Append new instructions entries based on existing data
        for _ in range(len(recipe.instructions)):
            form.instructions.append_entry()
        # Fill data for existing instructions entries
        for i, instruction_entry in enumerate(form.instructions.entries):
            instruction_entry.form.instruction.data = sorted(recipe.instructions, key=lambda x: x.step)[i].text
        form.picture.data = recipe.image_file
    return render_template('new_recipe.html', title="Update Recipe", form=form)


# Delete Recipes routes based on recipe id
@app.route('/recipe/<recipe_id>/delete', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def delete_recipe(recipe_id):
    """Deletes a recipe that matches the id given"""
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user != current_user:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe has been successfully deleted!', 'success')
    return redirect(url_for('recipe_feed'))


# routes for users profile
@app.route('/recipes/<string:username>', methods=['GET'], strict_slashes=False)
def user_recipes(username):
    """recipe feed page"""
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    user_recipes = Recipe.query.filter_by(user_id=user.id).order_by(Recipe.created_at.desc())\
                   .paginate(page=page, per_page=5)
    return render_template('user_recipes.html', user=user, title=f"{user.username} Recipes",
                           recipes=user_recipes)


if __name__ == "__main__":
    app.run(debug=True)
