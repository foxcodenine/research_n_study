from my_app import app, db

# ______________________________________________________________________

class Users(db.Model):
    __tablename__ = 'flask_admin_users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)

    user_comments = db.relationship('Comments', backref='user', lazy='dynamic')

    

    def __repr__(self):
        return '<Email {}>'.format(self.email)


    def __init__(self, email, password, age, birthday):
        self.email = email
        self.password = password + password
        self.age = age
        self.birthday = birthday

class Comments(db.Model):
    __tablename__ = 'flask_admin_comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('flask_admin_users.id'))  

    def __repr__(self):
        return '<Comment {}>'.format(self.id)  



    
