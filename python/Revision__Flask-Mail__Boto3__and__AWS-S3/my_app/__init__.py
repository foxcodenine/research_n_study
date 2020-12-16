from flask import Flask, redirect, render_template, url_for, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, send_from_directory
import os 
print('>>>>>>>>>>>>>',os.getcwd())

# ______________________________________________________________________




def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'development':
        app.config.from_object('config.ConfigDev')
    else:
        app.config.from_object('config.ConfigPro')
    return app 

app = create_app()

# ______________________________________________________________________
# Setting up flask_uploades

# Creating a set 

app_images = UploadSet('images', IMAGES)

email = 'chris12aug@yahoo.com'

# 

app.config['UPLOADED_IMAGES_DEST'] = f'{os.getcwd()}\\app_user_images\\{email}'

# note the name of the set "'photos'" should reflect ..ED_APPIMAGES_DE..

configure_uploads(app, app_images)

# ______________________________________________________________________

@app.route('/')
def index():
    return '{} {}'.format(app.config['CHECK_ENV'], app.config['SECRET_KEY'][::-1])

# _____________________


@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST' and 'thefile' in request.files:

        # Get the file from your html Form from input (name='thefile)
        image_filename = app_images.save(request.files['thefile'])

        # return f'<h5>{image_filename}</h5>' 
        # return f'<h5>{app_images.path(image_filename)}</h5>' 
        # return f'<h5>{app_images.url(image_filename)}</h5>'
        return send_from_directory(app.config['UPLOADED_IMAGES_DEST'], image_filename)
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
