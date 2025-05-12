from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(app=None, db=db)

login_manager = LoginManager()
login_manager.login_view = "frontend.login"
login_manager.login_message = "Please login or signup to add a new trip"
