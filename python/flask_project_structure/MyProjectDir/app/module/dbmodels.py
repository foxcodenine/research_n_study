from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Base(db.Model):
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
    password = db.Column(db.String(192),  nullable=False)
    role = db.Column(db.SmallInteger)


# # from app.module.models import db
# db.create_all()
# db.session.commit()