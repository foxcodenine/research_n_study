# send_from_directory
# https://www.kite.com/python/docs/flask.send_from_directory

# boto3
# https://realpython.com/python-boto3-aws-s3/
# ______________________________________________________________________

from flask import Flask, redirect, render_template, url_for, request, \
     send_from_directory, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os 

from flask_cors import CORS

import boto3
import uuid

# ______________________________________________________________________


def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == 'development':
        app.config.from_object('config.ConfigDev')
    else:
        app.config.from_object('config.ConfigPro')
    return app 

app = create_app()
CORS(app)
# ______________________________________________________________________
# ______________________________________________________________________
# Setting up flask_uploades

# Creating a set 
email = 'chris12aug@yahoo.com'

app_images = UploadSet('images', IMAGES) # <-(A)

app.config['UPLOADED_IMAGES_DEST'] = f'{os.getcwd()}\\app_user_images\\{email}' # <-(A)
# getcwd() returns current working directory of a process.

# (A) note the name of the set "'images'" should reflect ..ED_IMAGES_DE..

configure_uploads(app, app_images)

# ______________________________________________________________________

# Setting up boto3

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# Note. to access the client directly via the resource 
# s3_resource.meta.client

# ______________________________________________________________________
# ______________________________________________________________________

@app.route('/')
def index():
    # Root Route use for testing
    return '{} {}'.format(app.config['CHECK_ENV'], app.config['SECRET_KEY'][::-1])

# ______________________________________________________________________

# //----- Flast-Uploads Section -----//

# flask_uploades route. Upload from flask rendered_template to project folder, 
# using flask upload and display image in return.

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST' and 'thefile' in request.files:

        # Get the file from your html Form from input (name='thefile)
        image_file = request.files['thefile']
        image_filename = app_images.save(image_file)
       

        # return f'<h5>{image_filename}</h5>' #<- return file name
        # return f'<h5>{app_images.path(image_filename)}</h5>' # <- return path from project directory
        # return f'<h5>{app_images.url(image_filename)}</h5>'  # <- return image url from project directory


        return send_from_directory(app.config['UPLOADED_IMAGES_DEST'], image_filename, as_attachment=False) # <-display uploaded image
        # Send a file from a given directory with send_file(). This is a secure way to quickly
        # expose static files from an upload folder or something similar.
    
    return render_template('upload.html', action='upload')


# ______________________________________________________________________
# ______________________________________________________________________

# //----- Boto3 and AWS Section -----//

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])



def create_bucket(bucket_prefix, s3_connection):
    # Creating a bucket function   

    bucket_name = create_bucket_name(bucket_prefix)
    current_region = os.getenv('region')
    print('name>', bucket_name)

    bucket_response = s3_connection.create_bucket(

        Bucket = bucket_name,
        
        CreateBucketConfiguration = {
            'LocationConstraint': current_region
        })
    print('\n', bucket_name, current_region)

    return bucket_name, bucket_response    



@app.route('/create_s3/<s3>/<bucket_prefix>')
def create_s3(bucket_prefix, s3):
    
    if s3 == 's3r':
        s3_connection = s3_resource
    elif s3 == 's3c':
        s3_connection = s3_resource.meta.client


    first_bucket_name, first_response = create_bucket(bucket_prefix, s3_connection)

    return f'''
            <h4>AWS bucket name: {first_bucket_name}</h4>
            <h4>AWS response: {first_response}</h4>    
    '''
# _____________________________

# Boto3_upload route. Upload file from rendered_template with request.
# Files and send them with boto3, to aws s3

@app.route('/upload_s3', methods=['GET', 'POST'])
def upload_s3():
       

    if request.method == 'POST' and 'thefile' in request.files:
        image_file = request.files['thefile']

        my_bucket_name = 'flask-uploads-acfbfed9-5fae-490c-9d35-291c9af697b3'
        
        print('-->', image_file.__dict__)
        
        s3_resource.Bucket(my_bucket_name).put_object(
            Body = image_file,           # file to upload in bits
            Key = image_file.filename,   # file name to be save (& and subfolder)
            ACL = 'public-read'          # set to public
        )      
        

        return '<h2>...sent to aws!</h2>'

    return render_template('upload.html', action='upload_s3')
# ______________________________________________________________________
# ______________________________________________________________________


# Receiving image file from vue frontend and saving it with flask-uploads


@app.route('/upload_from_vue/', methods=['GET', 'POST'])
def upload_from_vue():
    
    if request.files:
        image_object = request.files['imageCover']
        image_name = request.form['imageName']
        image_filename = app_images.save(storage=image_object, folder=None, name=image_name)

        


    return jsonify({'message': '...image successfully uploaded to project folder!'})

'''
bucket name: flask-uploads-acfbfed9-5fae-490c-9d35-291c9af697b3

'''
# _____________________________

@app.route('/upload_from_vue_to_s3/', methods=['GET', 'POST'])
def upload_from_vue_to_s3():
    if request.method == 'POST' and request.files:
        image_object = request.files['imageCover']
        image_name = request.form['imageName']

        my_bucket_name = 'flask-uploads-acfbfed9-5fae-490c-9d35-291c9af697b3'



        s3_resource.Bucket(my_bucket_name).put_object(
            Body = image_object,
            Key = image_name ,
            ACL = 'public-read'
        )

        image_url = f'https://{my_bucket_name}.s3.{os.getenv("region")}.amazonaws.com/{image_name}'

        print(image_name)
        print(image_object)
    return jsonify({'message': '...image successfully uploaded to project folder!', 'image_url': image_url})
# ______________________________________________________________________
# ______________________________________________________________________

if __name__ == '__main__':
    app.run()