from app import app
from uuid import uuid4


app.config.from_object('config')
app.config['SECRET_KEY'] = uuid4().hex


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)