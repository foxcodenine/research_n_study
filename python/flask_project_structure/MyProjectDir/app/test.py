from flask import Flask, redirect, render_template, url_for, request
from flask_uploads import UploadSet, IMAGES, configure_uploads

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileAllowed, FileField
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'hgvdfjhsbjseh'
app.config['UPLOADED_PHOTOS_DEST'] = './aaaaaa'
configure_uploads(app, photos)
# ______________________________________________________________________

class AddUser(FlaskForm):

    name = StringField('Name', validators=[InputRequired(message='name required!')])

    surname = StringField('Surname', validators=[InputRequired(message='surname required!')])

    email = StringField('Email',validators=[InputRequired(message='email required!')])

    password = PasswordField('Password',validators==[InputRequired(message='password required!'), Length(min=6)])

    # image = FileField('Profile Image')



# ______________________________________________________________________
@app.route('/test', methods=['GET', 'POST'])
def test():
        
    form = AddUser()

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='sha256')
        
        image_filaname  = photos.save(request.files['filefile'])
        # image_url = photos.url(image_filaname)
           
        
        
        print('>>>', name, surname, email, password, image_filaname) 

        return redirect(url_for('test'))
    

    return render_template('public/signup.html', form=form)




if __name__ == '__main__':
    app.run()