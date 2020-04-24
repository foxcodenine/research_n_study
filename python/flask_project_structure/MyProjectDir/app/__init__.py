from flask import Flask, render_template, blueprints, url_for, request,\
    redirect
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_sqlalchemy import SQLAlchemy
from flask import abort

app = Flask(__name__, instance_relative_config=True)


photos = UploadSet('photos', IMAGES)

app.config.from_object('config')


configure_uploads(app, photos)
db = SQLAlchemy(app)

from .module.views import public_view, user_view
from app.module.dbmodels import db



# ______________________________________________________________________

app.register_blueprint(public_view)
app.register_blueprint(user_view)



@app.route('/')
def index():
    return render_template('index.html')


# ______________________________________________________________________

@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404 - Page Not Found', 404

@app.errorhandler(413)
def file_to_large(e):
    return "Error 404 - File to large", 413

# ______________________________________________________________________


db.create_all()


# ______________________________________________________________________

# 1. Add a render_template to error routes
