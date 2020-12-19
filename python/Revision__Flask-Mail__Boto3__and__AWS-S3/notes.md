flask_uploads: ImportError: cannot import name 'secure_filename'

https://stackoverflow.com/questions/61628503/flask-uploads-importerror-cannot-import-name-secure-filename

    In flask_uploads.py

    Change

    from werkzeug import secure_filename,FileStorage
    to

    from werkzeug.utils import secure_filename
    from werkzeug.datastructures import  FileStorage

OR 

    According to this issue, it is a bug related to the current version
    1.0.0 of workzeug. It's merged but not yet published in pypi. The
    workaround know until now is to downgrade from werkzeug=1.0.0 to
    werkzeug==0.16.0

<!-- --------------------------------------------------------------- -->

To install Boto3

    $ pip install boto3



<!-- --------------------------------------------------------------- -->
<!-- --------------------------------------------------------------- -->

OS functions
import os

Executing a shell command
os.system()    

Get the users environment 
os.environ()   

#Returns the current working directory.
os.getcwd()   

Return the real group id of the current process.
os.getgid()       

Return the current process’s user id.
os.getuid()    

Returns the real process ID of the current process.
os.getpid()     

Set the current numeric umask and return the previous umask.
os.umask(mask)   

Return information identifying the current operating system.
os.uname()     

Change the root directory of the current process to path.
os.chroot(path)   

Return a list of the entries in the directory given by path.Also, you can pass a parameter of a specific directory to view its file and sub-directory
os.listdir(path) 

Create a directory named path with numeric mode mode.
os.mkdir(path)    

Recursive directory creation function.
os.makedirs(path)  

Remove (delete) the file path.
os.remove(path)    

Remove directories recursively.
os.removedirs(path) 

Rename the file or directory src to dst.
os.rename(src, dst)  

Remove (delete) the directory path.
os.rmdir(path) 


os.chdir( )
This OS method is used to change the current directory into a new directory, it receives one parameter which is the path of the new directory.



os.rmdir( )
This OS method is used to remove a directory it receives an argument of the name of the directory you want to remove. os.rmdir() will only work for empty dirs

os.sytem ( )
This OS Method is used to run a shell command on the python program as if you were in shell. For instance, let’s run a tree command using the system method.

os.uname ( )
This OS Method returns information identifying the current operating system.




os.environ []
environ is not a method in the OS module rather than it’s a process parameter through which we can access the environment variables of the system.

For instance Let’s access environment variable HOME
    >>> import os
    >>> os.environ['HOME']
    
    '/home/kalebu'
    >>> os.environ['my_secret_key'] = "Life sucks" #setting our own variable