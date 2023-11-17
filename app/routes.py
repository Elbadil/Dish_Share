#!/usr/bin/python3
"""Main routes for the web app"""
from flask import Flask, render_template
import requests
import models


# Flask app
app = Flask(__name__)


# home route
@app.route('/home', strict_slashes=False)
def home():
    """home page"""
    return "<h1>Home Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
