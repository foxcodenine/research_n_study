from app import db, UserMixin

class Base(UserMixin, db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
                    db.DateTime, default=db.func.current_timestamp())

    date_modified = db.Column(
                    db.DateTime,  
                    default=db.func.current_timestamp(), 
                    onupdate=db.func.current_timestamp())


class Users(Base):
    __tablename__ = 'users'
    
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(250),  nullable=False)
    image = db.Column(db.String(250),  nullable=False)
    role = db.Column(db.SmallInteger)

    def __init__(self, name, surname, email, password, image, role=0):

        self.name = name 
        self.surname = surname 
        self.email = email 
        self.password = password 
        self.image = image
        self.role =role
    


# # from app.module.models import db
# db.create_all()
# db.session.commit()