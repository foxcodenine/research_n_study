from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, HiddenField, \
    PasswordField, BooleanField
from wtforms.validators import Length, InputRequired, Email
from flask_uploads import IMAGES


import string

# ______________________________________________________________________

def pass_val(_str):
    """Chk if a string contains an lowerCase, upperCase and digit char."""

    string_list = []
    for s in _str:
        string_list.append(s)

    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    num   = list(string.digits)

    dic = { 'lower': [lower, False], 
            'upper':[upper, False], 
            'num': [num, False]}

    for k, v in dic.items():
            
            for x in v[0]:
                v[1] = x in string_list
                if v[1] == True:
                    break

    if dic['lower'][1] * dic['upper'][1] * dic['num'][1]:
        return True 
    else:
        return False
# ______________________________________________________________________
    

class AddUser(FlaskForm):

    # In template <forms> remember to add enctype="multipart/form-data" AND novalidate

    name = StringField('Name', validators=[InputRequired(message='name required!')])

    surname = StringField('Surname', validators=[InputRequired(message='surname required!')])

    email = StringField('Email',validators=[InputRequired(message='email required!'), Email()])

    password = PasswordField('Password',validators=[InputRequired(message='password required!'), Length(min=6)])

    image = FileField('Profile Image')


# ______________________________________________________________________


class LoginUser(FlaskForm):
    email = StringField('Email', validators=[InputRequired('Username is required!')])
    password = PasswordField('Password', validators=[InputRequired('Password is required!')])
    remember = BooleanField('Remember me')




