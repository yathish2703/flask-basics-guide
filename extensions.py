"""
Flask Extensions
Initialize Flask extensions here to avoid circular imports
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions without app
db = SQLAlchemy()
login_manager = LoginManager()
