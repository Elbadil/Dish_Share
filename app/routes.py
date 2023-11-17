#!/usr/bin/python3
"""Main routes for the web app"""
from flask import Flask, render_template
from models.recipe import Recipe
import requests
import models


# Flask app
app = Flask(__name__)


# recipe feed route
@app.route('/')
@app.route('/recipe_feed', strict_slashes=False)
def recipe_feed():
    """recipe feed page"""
    recipes = models.storage.all(Recipe)
    return render_template('feed.html', recipes=recipes)


if __name__ == "__main__":
    app.run(debug=True)
