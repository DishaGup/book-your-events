#models.py

from app import db
import sys
import os

# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flask_mongoengine import MongoEngine


class User(db.Document):
    """
    This class represents a user in the application.

    Attributes:
        username (str): The username of the user.
        user_status (bool): The status of the user.
        gender (str): The gender of the user.
        membership_type (str): The membership type of the user.
        bio (str): The bio of the user.
        date_of_birth (datetime): The date of birth of the user.
        location (str): The location of the user.
    """
    username = db.StringField(required=True, unique=True)
    user_status = db.BooleanField(default=True)
    gender = db.StringField(choices=['Male', 'Female', 'Other'])
    membership_type = db.StringField(choices=['Regular', 'Premium', 'VIP'])
    bio = db.StringField()
    date_of_birth = db.DateTimeField()
    location = db.StringField(required=True)

class Movie(db.Document):
    title = db.StringField(required=True)
    rating = db.DecimalField()
    description = db.StringField(required=True)
    genre = db.StringField()
    duration = db.StringField()
    cast = db.ListField(db.StringField())

class Show(db.Document):
    movie = db.ReferenceField(Movie, required=True, reverse_delete_rule=db.CASCADE)
    timings = db.ListField(db.DateTimeField())
    categories = db.ListField(db.StringField())
    location = db.StringField()

class Event(db.Document):
    name = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    participants = db.ListField(db.ReferenceField('Participant'))
    ticket_price = db.DecimalField()
    venue = db.StringField()
    description = db.StringField()

class Participant(db.Document):
    name = db.StringField(required=True)
    events = db.ListField(db.ReferenceField(Event))
    email = db.EmailField()
    phoneno = db.StringField()
    address = db.StringField()
