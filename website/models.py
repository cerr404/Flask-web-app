from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# these classes are representing our database modles fro users and notes

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) # this column is the primary key for Note modle
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Forein Key to link each note to a specific user in User model


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200), nullable= False)
    first_name = db.Column(db.String(100))
    # Means a user can have multiple notes and signifies the one-to-many relation
    notes = db.relationship('Note')
