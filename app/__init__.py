#!/usr/bin/python3
"""Main app and database"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# App MySQL Database
if os.getenv('TESTS'):
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DS_DB_TEST_LINK')
    app.config['WTF_CSRF_ENABLED'] = False
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DS_DB_LINK')
db = SQLAlchemy(app)

# Password hashing Instance
bcrypt = Bcrypt(app)

# Login Manager for users logins
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
