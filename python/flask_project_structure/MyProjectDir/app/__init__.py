from flask import Flask, render_template, blueprints, url_for, request,\
    redirect
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_sqlalchemy import SQLAlchemy
from  flask_login import LoginManager, UserMixin, login_user ,login_required, \
    logout_user, logout_user, current_user, logout_user
from flask import abort

from logging import FileHandler, WARNING

from flask_caching import Cache




app = Flask(__name__, instance_relative_config=True)




# setup flask-uploads set (the set it the var photo, 
#                         'photos' is the name used in UPLOADED_PHOTOS_DEST
#                          IMAGES is the type)
photos = UploadSet('photos', IMAGES)

app.config.from_object('config')

# https://flask.palletsprojects.com/en/1.1.x/logging/#basic-configuration
if not app.debug:
    file_handler = FileHandler('errorlog.txt')
    file_handler.setLevel(WARNING)

    app.logger.addHandler(file_handler)

# setup flask-uploads
configure_uploads(app, photos)

# setup sqlalchemy db
db = SQLAlchemy(app) 

#setup flask_cache
app.config["CACHE_TYPE"] = 'simple'
#app.config["CACHE_DEFAULT_TIMEOUT"] = 3000
cache = Cache(app)

# setup flask-login 
login_manager = LoginManager(app)
login_manager.login_view = 'public_view.login' # <- this  redirect to 'login' if @login_required fails.

# need to be after app before app.register_blueprint()
from .module.views import public_view, user_view
from app.module.dbmodels import Users


# ______________________________________________________________________

app.register_blueprint(public_view)
app.register_blueprint(user_view)


# ______________________________________________________________________

@app.route('/')
def index():

    user = False
    profiles = None

    try:
        if current_user.id:
            user = True

            profiles = Users.query.all()
    

    except AttributeError:        
        pass

    
    return render_template('index.html', user=user, profiles=profiles)


# ______________________________________________________________________

@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404 - Page Not Found', 404

@app.errorhandler(413)
def file_to_large(e):
    return "Error 413 - File to large", 413

# ______________________________________________________________________

from app.module.dbmodels import db
db.create_all()


# ______________________________________________________________________

# 1. Add a render_template to error routes
