from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# Initialize Flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = '609d12b4c1ed18916f3479c5'  # Generates a 64-character key


# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'


# Initialize Extensions
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login_page"

# Import Routes (To avoid circular imports)
from market import routes
