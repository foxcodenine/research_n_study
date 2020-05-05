from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from app import photos
from app import db
from app import login_manager ,login_user, login_required, current_user,\
logout_user

from app.module.dbmodels import Users
from app.module.forms import AddUser, LoginUser


# ______________________________________________________________________

public_view = Blueprint('public_view', __name__, url_prefix='/public')
user_view = Blueprint('user_view', __name__, url_prefix='/user')


# ______________________________________________________________________

@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(int(user_id))

# ______________________________________________________________________
@public_view.route('/signup', methods=['POST', 'GET'])
def signup():

    form = AddUser(CSRF_ENABLED = True)

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='sha256')        
        image_filename = photos.save(form.image.data)
        image_url = 'profile_images/{}'.format(image_filename)

        chk_email = Users.query.filter_by(email=email).first()
        if chk_email:
            flash('Email already used!')
            return redirect(url_for('public_view.signup'))

        newUser = Users(name, surname, email, password, image_url, role=0)
        db.session.add(newUser)
        db.session.commit()                                  
        login_user(newUser)
        return redirect(url_for('user_view.profile'))    

    return render_template('public/signup.html', form=form)
# ______________________________________________________________________

@public_view.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginUser(CSRF_ENABLED = True)

    if form.validate_on_submit():

        email = form.email.data 

        logged_user = Users.query.filter_by(email=email).first()

        if logged_user == None:
            flash('Email provided is not registered')         
            return redirect(url_for('public_view.login'))
        
        
        password = form.password.data

        if check_password_hash(logged_user.password, password):
            remember = form.remember.data
          
            login_user(logged_user, remember=remember)
            return redirect(url_for('user_view.profile'))
        else :
            flash('Password incorrect')
            return redirect(url_for('public_view.login'))


    return render_template('public/login.html', form=form)

# ______________________________________________________________________


@user_view.route('/profile')
@login_required
def profile():
    user = current_user
    
    return render_template('user/profile.html', user=user)

# ______________________________________________________________________
@user_view.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# ______________________________________________________________________




