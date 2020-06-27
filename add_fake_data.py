from datetime import datetime
from app import app
from models import Event, Volunteer, Artist, db


event = Event(
    name='Wetfoot Festival 2019',
    phone_number='555-555-5555',
    email = 'wisehall@gmail.com',
    start_time=datetime(2020, 4, 25, 17, 40, 19, 448277),
    end_time=datetime(2020, 4, 26, 1, 30, 19, 448277),
    venue_name = 'The Wisehall',
    theme='Major Tom Goes to Wonderland',
    website='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
)

add_list = [event]
[db.session.add(item) for item in add_list]
db.session.commit()


artist = Artist(
    name="Justin Beiberlake",
    phone_number='555-555-5556',
    email = 'jbl@gmail.com',
    event =1,
    genres=["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    website='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    instagram_link='https://www.facebook.com/joeexotic',
    image_link="https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
)

artist2 = Artist(
    name="Gnarfunkel",
    phone_number='555-555-5557',
    email = 'gnarfunkelband@gmail.com',
    event =1,
    genres=["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    website='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    instagram_link='https://www.facebook.com/joeexotic',
    image_link="https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
)

volunteer = Volunteer(
    name="Tyler",
    phone_number='555-555-5558',
    email = 'tyler@gmail.com',
    event =1
)

volunteer2 = Volunteer(
    name="Annie",
    phone_number='555-555-5559',
    email = 'annie@gmail.com',
    event =1
)

add_list = [volunteer, volunteer2, artist, artist2]
[db.session.add(item) for item in add_list]
db.session.commit()
db.session.close()