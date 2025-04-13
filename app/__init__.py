import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Create the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Ensure the uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import views and models
from app import views, models
