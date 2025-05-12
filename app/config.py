import os
import pathlib


class BaseConfig(object):
    PROJECT = "flask-project"
    PROJECT_NAME = "flask-project.domain"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = False
    TESTING = False

    SECRET_KEY = "always-change-this-secret-key-with-random-alpha-nums"


class DefaultConfig(BaseConfig):
    BASE_URL = "localhost"
    DEBUG = True

    # Flask-Sqlalchemy
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


class ProductionConfig(BaseConfig):
    BASE_URL = "https://yourdomain-flaskstarter.domain"
    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:pass@ip/dbname"
