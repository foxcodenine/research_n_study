# https://www.youtube.com/watch?v=2dEM-s3mRLE&t=15s

# ______________________________________________________________________

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, fresh_login_required

from urllib.parse import urljoin, urlparse

from datetime import timedelta, datetime

from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from itsdangerous.exc import SignatureExpired
# ______________________________________________________________________

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# ______________________________________________________________________

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['FLASK_ENV'] = os.getenv("FLASK_ENV")
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_CONNECTION')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=20) #<- not working in chrome

db = SQLAlchemy(app)
serializer = URLSafeTimedSerializer(app.secret_key)

# ______________________________________________________________________
# Setup LoginManager 

login_manager = LoginManager(app)
login_manager.login_view = 'login_form'
login_manager.login_message = 'You can\'t access that page. You need to login first.'

@login_manager.user_loader
def load_user(session_token):
    user = Users.query.filter_by(session_token=session_token).first()
    try:
        serializer.loads(session_token, max_age=10) # <- expire after a day
    except SignatureExpired:
        if user:
            user.session_token = None
            db.session.commit()
        return None
    return user

# ______________________________________________________________________
# Database Class

class Users(UserMixin, db.Model):
    __tablename__ = 'flask_login_users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime)
    session_token = db.Column(db.String(255), unique=True)
    

    def __init__(self, email, password):
        self.email = email
        self.username = email
        self.password = password
        self.created = datetime.now()
        self.session_token = serializer.dumps([self.email, self.password])

    def get_id(self):
        return self.session_token

    def update_password(self, password):
        self.password = password
        self.session_token = serializer.dumps([self.email, self.password])

    def update_email(self, email):
        self.email = email
        self.session_token = serializer.dumps([self.email, self.password])

    def update_session_token(self):
        self.session_token = serializer.dumps([self.email, self.password])

# ______________________________________________________________________
# Helper function

def is_safe_url(target):
    # check if :
    #   url has http or https 
    #   if url is on my server
    #   and target is not None

    ref_url  = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))

    return  test_url.scheme in ('http', 'https') and \
            ref_url.netloc == test_url.netloc and \
            target != None



# ______________________________________________________________________
# Routes

@app.route('/')
def index():
    return 'so far so good! {}'.format(app.__dir__())

# _________________________________


@app.route('/login_form',  methods=['GET', 'POST'])
def login_form():

    # ---- redirect if already siged in__________________
    if current_user.is_authenticated == True:
        return redirect(url_for('home'))
    # ____ if POST_______________________________________

    if request.method == 'POST':

        username = request.form['username']


        user = Users.query.filter_by(username=username).first()

        if user:
            user.update_session_token()
            db.session.commit()
            login_user(user, remember=True)  # <- set user obj in login_user 
                                             #    and remember to persist 
                                             #    user if browser exit

            if 'next' in session and is_safe_url(session['next']):  # <- redirect (next)
                return redirect(session['next'])                    # <- redirect (next)
            else:
                return redirect(url_for('home'))
        
        else:
            flash(f'{username} - Invalid username!')


    session['next'] = request.args.get('next')      # <- redirect (next)

    return render_template('login.html')
# _________________________________


@app.route('/logout/')
def logout():
    logout_user()
    return '<h2>You are now loged out!</h2>'

# _________________________________


@app.route('/home/')
@login_required
def home():
    return '<h2>Hi {}! You are in the protected area!</h2>'.format(current_user.username)


@app.route('/fresh/') # does not work in chrome 
@fresh_login_required
def fresh():
    return '<h2>Fresh login router!</h2>'

# ______________________________________________________________________


if __name__ == '__main__':
    app.run()