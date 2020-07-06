from datetime import datetime
from app import app
from models import Event, Volunteer, Artist, db


event = Event(
    name='Wetfoot Festival 2019',
    phone_number='555-555-5555',
    email='wisehall@gmail.com',
    venue_name='The Wisehall',
    theme='Major Tom Goes to Wonderland',
    website='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
)

event2 = Event(
    name='Wetfoot Festival 2020',
    phone_number='555-555-5535',
    email='wisesthall@gmail.com',
    venue_name='The Wisesthall',
    theme='Major Tom Goes Fishing',
    website='https://www.netflix.com',
)

add_list = [event, event2]
[db.session.add(item) for item in add_list]
db.session.commit()


artist = Artist(
    name="Justin Beiberlake",
    phone_number='555-555-5556',
    email='jbl@gmail.com',
    event=1,
    website='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    instagram_link='https://www.facebook.com/joeexotic',
    image_link="https://images.unsplash.com/photo-14"
)

artist2 = Artist(
    name="Gnarfunkel",
    phone_number='555-555-5557',
    email='gnarfunkelband@gmail.com',
    event=1,
    website='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    instagram_link='https://www.facebook.com/joeexotic',
    image_link="https://images.unsplash.com/photo-15"
)

volunteer = Volunteer(
    name="Tyler",
    phone_number='555-555-5558',
    email='tyler@gmail.com',
    event=1
)

volunteer2 = Volunteer(
    name="Annie",
    phone_number='555-555-5559',
    email='annie@gmail.com',
    event=1
)

add_list = [volunteer, volunteer2, artist, artist2]
[db.session.add(item) for item in add_list]
db.session.commit()
db.session.close()
