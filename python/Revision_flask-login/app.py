# https://www.youtube.com/watch?v=2dEM-s3mRLE&t=15s

# ______________________________________________________________________

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

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



db = SQLAlchemy(app)

# ______________________________________________________________________
# Setup LoginManager 

login_manager = LoginManager(app)
login_manager.login_view = 'login_form'
login_manager.login_message = 'You can\'t access that page. You need to login first.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ______________________________________________________________________
# Database Class

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)

# ______________________________________________________________________
# Routes

@app.route('/')
def index():
    return 'so far so good! {}'.format(os.getenv('SECRET_KEY'))

# _________________________________

@app.route('/login/<username>/')
def login(username):
    user = User.query.filter_by(username=username).first()

    if user:
        login_user(user)
        return '<h2>{} - Logged In!</h2>'.format(user.username)
    else:
        return '<h2>{} - Invalid username!</h2>'.format(username)
# _________________________________




@app.route('/login_form',  methods=['GET', 'POST'])
def login_form():

    # ---- redirect if already siged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # _________________________________
    if request.method == 'POST':
        username = request.form['username']

        user = User.query.filter_by(username=username).first()
        if user:
            login_user(user)

            if 'next' in session and session['next'] != None:   # <- redirect (next)
                return redirect(session['next'])                # <- redirect (next)
            else:
                return '<h2>{} - Logged In!</h2>'.format(user.username)
        
        else:
            flash(f'{username} - Invalid username!')

    session['next'] = request.args.get('next')      # <- redirect (next)

    return render_template('login.html')
# _________________________________


@app.route('/logout')
def logout():
    logout_user()
    return '<h2>You are now loged out!</h2>'

# _________________________________

@app.route('/protected')
@login_required
def protected():
    return '<h2>Hi {}! You are in the protected area!</h2>'.format(current_user.username)

# ______________________________________________________________________


if __name__ == '__main__':
    app.run()