# from sqlalchemy.orm import backref
from . import db
# from datetime import datetime

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    full_name = db.Column(db.String(225))
    username = db.Column(db.String(225))
    email = db.Column(db.String(225), unique=True)
    password = db.Column(db.String(225))
    password_token = db.Column(db.Boolean)