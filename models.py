from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class CommonModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email}


class Volunteer(CommonModel):
    __tablename__ = 'volunteers'

    event = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

    def __repr__(self):
        return f'<Volunteer ID: {self.id} Name: {self.name}>'


class Artist(CommonModel):
    __tablename__ = 'artists'

    # Arrays works for postsgres, but not everything.
    genres = db.Column(db.ARRAY(db.String()))
    event = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    website = db.Column(db.String(200))
    instagram_page = db.Column(db.String(200))
    
    #TODO: This will eventually need to be something that they upload.
    image_link = db.Column(db.String(500))

    def __repr__(self):
        return f'<Artist ID: {self.id} Name: {self.name}>'


class Event(CommonModel):
    __tablename__ = 'events'

    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    venue_name = db.Column(db.String, nullable=False)
    artists = db.relationship('Artist', backref='event', lazy=True)
    volunteers = db.relationship('Volunteer', backref='event', lazy=True)

    def __repr__(self):
        return f'<Event ID: {self.id} Venue Name: {self.venue_name} Start Time: {self.start_time}>'