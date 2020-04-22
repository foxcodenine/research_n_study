from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, HiddenField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES
import string
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
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

    name = StringField('Name')
    surname = StringField('Surname')
    email = StringField('Email')
    password = PasswordField('Password')
    profile_pic = FileField('Profile Image', validators=[FileAllowed(IMAGES)])
