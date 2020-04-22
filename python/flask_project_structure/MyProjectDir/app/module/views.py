from flask import Blueprint, render_template, request, redirect, url_for
from app.module.forms import AddUser
from werkzeug.security import generate_password_hash, check_password_hash

public_view = Blueprint('public_view', __name__, url_prefix='/public')

user_view = Blueprint('user_view', __name__, url_prefix='/user')

# ______________________________________________________________________


@public_view.route('/signup', methods=['POST', 'GET'])
def signup():

    form = AddUser()

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='sha256')
        print('>>>', name, surname, email, password) 

        return redirect(url_for('index'))

    

    return render_template('public/signup.html', form=form)

# ______________________________________________________________________

@public_view.route('/login')
def login():
    return render_template('public/login.html')

# ______________________________________________________________________


@user_view.route('/profile')
def profile():
    return render_template('user/profile.html')

# ______________________________________________________________________