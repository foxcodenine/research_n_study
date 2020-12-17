# _________________________________________

import os
from dotenv import load_dotenv

# os.path.expanduser(path)

# On Unix and Windows, return the argument with an initial component of ~ or
# ~user replaced by that user’s home directory.

# print('->', os.getcwd())
# print('->', os.path.expanduser(os.getcwd()))

project_folder = os.path.expanduser(os.getcwd())
load_dotenv(os.path.join(project_folder, '.env'))


print('->', os.environ['aws_access_key_id'])

# _________________________________________

from my_app import app 

if __name__ == "__main__":
    app.run()