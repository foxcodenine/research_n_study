from flask import Flask, render_template, blueprints, url_for

from .module.views import public_view, user_view


app = Flask(__name__)
app.config.from_object('config')

# ______________________________________________________________________


app.register_blueprint(public_view)
app.register_blueprint(user_view)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login')
def login():
    return render_template('public/login.html')




# ______________________________________________________________________

from app.module.dbmodels import db
db.create_all()
