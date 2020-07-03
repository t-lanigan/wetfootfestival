from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=os.environ['DATABASE_URL']):

    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class CommonModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Volunteer(CommonModel):
    __tablename__ = 'volunteers'

    event = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'event': self.event
        }

    def __repr__(self):
        return json.dumps(self.format())


class Artist(CommonModel):
    __tablename__ = 'artists'

    event = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    # Arrays works for postsgres, but not everything.
    # genres = db.Column(db.ARRAY(db.String()))

    website = db.Column(db.String(200))
    instagram_link = db.Column(db.String(500))

    # TODO: This will eventually need to be something that they upload.
    image_link = db.Column(db.String(500))

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'event': self.event,
            'website': self.website,
            'instagram_link': self.instagram_link,
            'image_link': self.image_link
        }

    def __repr__(self):
        return json.dumps(self.format())


class Event(CommonModel):
    __tablename__ = 'events'

    venue_name = db.Column(db.String, nullable=False)
    artists = db.relationship('Artist', backref='artist_event', lazy=True)
    volunteers = db.relationship(
        'Volunteer', backref='volunteer_event', lazy=True)
    theme = db.Column(db.String, nullable=False)
    website = db.Column(db.String(200))

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'artists': [artist.format() for artist in self.artists],
            'volunteers': [volunteer.format() for volunteer in self.volunteers],
            'venue_name': self.venue_name,
            'theme': self.theme,
            'website': self.website}

    def __repr__(self):
        return json.dumps(self.format())
