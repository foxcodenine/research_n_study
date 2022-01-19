import os
from dotenv import load_dotenv

# _________________________________________

project_folder = os.path.expanduser(os.getcwd())
load_dotenv(os.path.join(project_folder, '.env'))

# _________________________________________

from my_app import app

if __name__ == "__main__":
    app.run(host=os.getenv('FLAKS_RUN_HOST'), port=os.getenv('FLASK_RUN_PORT'))