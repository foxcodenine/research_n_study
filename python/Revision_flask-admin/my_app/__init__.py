
# ______________________________________________________________________
# Imports

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# ______________________________________________________________________
# App Setup

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'development':
        app.config.from_object('config.ConfigDev')
    else:
        app.config.from_object('config.ConfigPro')
    
    return app

app = create_app()
CORS(app)
db = SQLAlchemy(app)



# ______________________________________________________________________

# General Routes
@app.route('/')

def index():
    return '{} - {}'.format(app.env, app.config['SECRET_KEY'][::-1])

# ______________________________________________________________________