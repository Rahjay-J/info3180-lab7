import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env if it exists.

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')  # Secure it in production
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', os.path.join(basedir, 'uploads'))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost/lab5').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress the SQLAlchemy warning
