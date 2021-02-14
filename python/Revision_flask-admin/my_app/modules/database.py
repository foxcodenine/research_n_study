from my_app import app, db, ModelView, bcrypt

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
        

# _____________________________________

class UserView(ModelView):
    # https://flask-admin.readthedocs.io/en/latest/api/mod_model/

    column_exclude_list = ('password')
    # column_list = ('id', 'email', 'age', 'birthday')
    column_display_pk = True
    column_labels = dict(id='User ID', birthday='Date of Birth')
    can_delete = True
    can_edit = True 
    can_create = True
    can_export = True
    column_searchable_list = ('id','email')
    create_modal = True


    def on_model_change(self, form, model, is_created):
        # Perform some actions before a model is created or updated and
        # committed to the database.
        model.password = bcrypt.generate_password_hash(model.password).decode('utf-8')

    def after_model_change(self, form, model, is_created):
        # Perform some actions after a model was created or updated and
        # committed to the database.
        pass

# _____________________________________

class Comments(db.Model):
    __tablename__ = 'flask_admin_comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('flask_admin_users.id'))  

    def __repr__(self):
        return '<Comment {}>'.format(self.id)  



    
