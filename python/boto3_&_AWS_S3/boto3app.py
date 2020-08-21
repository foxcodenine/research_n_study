# https://realpython.com/python-boto3-aws-s3/
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html#downloading-files
# https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/s3-example-download-file.html
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

# ______________________________________________________________________

import boto3
from uuid import uuid4

# ______________________________________________________________________

    # Connecting:

    # Client: low-level service access
    # Resource: higher-level object-oriented service access

s3_client = boto3.client('s3')

# or

s3_resource = boto3.resource('s3')

    # You can access the client directly via the resource like so:
    # s3_resource.meta.client.


# ______________________________________________________________________

# Print out bucket names

for bucket in s3_resource.buckets.all():
    print('---> {}'.format(bucket.name))

# # ______________________________________________________________________

#     # Creating a Bucket



# def create_bucket_name(bucket_prefix):
#     ''' Genarated unique bucket name, with a give prefix
#         Bucket name must be between 3 & 63 chars long'''

#     return ''.join([bucket_prefix, str(uuid4())])




#     # code example to create a bucket {
#     #
#     #   s3_resource,create_bucket(Bucket=YOUR_BUCKET_NAME,
#     #                               CreateBucketConfiguration={
#     #                               'LocationConstraint': 'eu-west-1'})
#     #
#     # }


# # You need to provide both a bucket name and a bucket configuration where
# # you must specify the region, which in my case is eu-west-1.



#     # get region from boto3 session {
#     #
#     #   session = boto.session.Session()
#     #   current_region = session.region_name
#     #
#     # }


# def cearte_bucket(bucket_prefix, s3_connection):
#     ''' Func. crate s3 bucket.
#         s3_connection, client or resource.
#     '''

#     current_region = boto3.session.Session().region_name

#     bucket_name = create_bucket_name(bucket_prefix)

#     bucket_response = s3_connection.create_bucket(

#         Bucket=bucket_name,
#         CreateBucketConfiguration={
#             'LocationConstraint': current_region
#         }
#     )
#     print(bucket_name, current_region)
#     return bucket_name, bucket_response



# # Createing my 1st 2 bucket, useing client and resource respectivly:


# # first_bucket_name, first_response = cearte_bucket(
# #                                 bucket_prefix='1st-python-bucket-',
# #                                 s3_connection=s3_resource.meta.client)

# # second_bucket_name, first_response = cearte_bucket(
# #                                 bucket_prefix='2nd-python-bucket-',
# #                                 s3_connection=s3_resource)



# # ______________________________________________________________________

#     # Add files to Buckets

# def create_temp_file(size, file_name, file_content):
#     ''' Funct. create a sample file with a random filename prefix'''

#     random_file_name = ''.join([str(uuid4().hex[:6]), '-', file_name])

#     with open(random_file_name, 'w') as f:
#         f.write(str(file_content) * size)
#     return random_file_name



# my1st_file = create_temp_file(1, 'chrisX1.txt', '_Chris_Farrugia_')




#     # Creating Bucket and Object Instances




# my1st_bucket = s3_resource.Bucket(name='1st-python-bucket-7b4cc0b3-1854-4502-9f83-e692ad6f757d')
# # Note: Here I am hard code the bucket name, however you have access to
# # the bucket name when it is created.

# my1st_object = s3_resource.Object(
#     bucket_name = '1st-python-bucket-7b4cc0b3-1854-4502-9f83-e692ad6f757d',
#     key = my1st_file
# )
# # ______________________________________________________________________

#     # Understanding Sub-resources
#     # Bucket and Object are sub-resources of one another.



# # If you have a Bucket variable, you can create an Object directly:

# my1st_object_again = my1st_bucket.Object(my1st_file)


# # Or if you have an Object variable, then you can get the Bucket:

# my1st_bucket_again = my1st_object.Bucket()



# # ______________________________________________________________________


#     # Uploading a File

#     # There are three ways you can upload a file:

#     #     From an Object instance
#     #     From a Bucket instance
#     #     From the client

# # ______________________________________

# Object Instance Version

# bucket_name = '1st-python-bucket-7b4cc0b3-1854-4502-9f83-e692ad6f757d'

# first_file = create_temp_file(2, 'chrisX2.txt', '_Chris_Farrugia_')

# s3_resource.Object(bucket_name, first_file).upload_file(Filename=first_file)

# # Or you can use the first_object instance however you'll save with the
# # object filename:

# my1st_object_again.upload_file(Filename=first_file)

# # ______________________________________

# # Bucket Instance Version

# third_file = create_temp_file(3, 'chrisX3.txt', '_Chris_Farrugia_')

# s3_resource.Bucket(bucket_name).upload_file(
#     Filename=third_file, Key=third_file
# )

# # ______________________________________

# Upload from pc using bucket version
bucket_name = '1st-python-bucket-7b4cc0b3-1854-4502-9f83-e692ad6f757d'

file_path = './static/ghost.jpg'



s3_resource.Bucket(bucket_name).upload_file(
    Filename=file_path ,
    Key = 'my_ghost.jpg'
)

# OR

my_file = open('./static/fox.jpg', 'rb')

print(my_file)

s3_resource.Bucket(bucket_name).put_object(
    Body = my_file,
    Key = 'create_subfolder/fox.jpg'
)


# ______________________________________


# Client Version


# --- getting data---
my_file = './static/5IBOJj.jpg'

file_name = my_file.split('/')[-1]

subfolder = 'FOXCODE'

print(file_name)


# --- uploading file---
s3_resource.meta.client.upload_file(
    Filename = my_file,
    Bucket = bucket_name,
    Key = f'{subfolder}/{file_name}'
)

# ______________________________________

# Set file to public when upload:

s3_resource.Bucket(bucket_name).upload_file(
    './static/hollow_knight.jpeg',
    Key='Hollow_Knight.jpeg',
    ExtraArgs={'ACL': 'public-read'}
)
# or

# s3_resource.Bucket(mybucket).put_object(
#             Body = form.image.data,
#             Key = f'{subfolder}/{image_name}',
#             ACL = 'public-read'
#         )


# ______________________________________________________________________

    # Downloading a File

file_in_bucket = 'my_ghost.jpg'

bucket_name = '1st-python-bucket-7b4cc0b3-1854-4502-9f83-e692ad6f757d'



# download by Bucket


s3_resource.Bucket(bucket_name).download_file(

    file_in_bucket,
    f'./static/download/rev1-{file_in_bucket}'
)


# download by Object

s3_resource.Object(bucket_name, file_in_bucket).download_file(
    f'./static/download/rev2-{file_in_bucket}'
)
