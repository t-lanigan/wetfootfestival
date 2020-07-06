# Wetfoot Festival

The Wetfoot Festival Website! Wetfoot festival is a festival that happens every year in Vancvouer, BC. This website allow for admins to create the festival every year and for artists and volunteers to sign up to contribute.

## Signing in

Visit `https://wetfootfestival.herokuapp.com/login`.

See RBAC section below for example usernames and passwords.

## Technologies
Python3
Flask
Postgres
SQLAlchemy
Flask-SQLAlchemy
psycopg2
Flask-Migrate
alembic

## Installation

```
git clone https://github.com/t-lanigan/wetfootfestival.git
conda create --name wetfootfestival python=3.6
source activate wetfootfestival
make deps
```

Create the database using:

`createdb wetfootfestival`


## Usage
Run the command below to start the app.

`make run`

or

`FLASK_APP=app.py FLASK_ENV=development flask run`

## Unit tests

To run the unittest suit use:

`make test`

__NOTE:__ In order to run the test suit you need an active token from login in. This must then be put in the setup.sh file for ADMIN_TOKEN. For the purposes of testing, one has been provided.


## Running migrations
Use the following commands to run database migrations to add tables or columns (not nessesary for tests)

* `make init-db`
* `make migrate-db`
* `make upgrade-db`

## Test Live Site

You can try testing the live endpoint using:

`curl https://wetfootfestival.herokuapp.com/events`

To test endpoints requiring permissions a requets using the following header must be included

`"Authorization": "Bearer <TOKEN>"`

The token that can be used is:

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhUUWJaTlZnYzVMVFVxdHFzU2t2YyJ9.eyJpc3MiOiJodHRwczovL3R5bGVycy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzM5NDcwMTI4MjUzNTgyNTk1OSIsImF1ZCI6IndldGZvb3RmZXN0aXZhbCIsImlhdCI6MTU5Mzc0ODc1NSwiZXhwIjoxNTkzODM1MTU1LCJhenAiOiJMRmxpbm40WUN5MkxObkpkenc2YzBrMnVPd2w1OW5LSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWZmZWN0OmFydGlzdHMiLCJhZmZlY3Q6ZXZlbnRzIiwiYWZmZWN0OnZvbHVudGVlcnMiXX0.TMKu_ap8jlMKlWwKKxDAI-IATRRatWNId1AEdjtGEwExuKU2zrJeSeUIC9pjHDmbS0CHwt9Fn-xKDq2it9XqdIQv_ufMyijPGkO7Siv8tE2j5dBVbj_XHYTbuR73QnO8Pxk29x4RDF5TfcY3JwL2HV6MlYpFzgwNIZbQ0PggjP6yaRc5ugowPSVRrOM_TFN-WXB2QQiiByNJXrKU0gLql4IXyHgnkw7pcMeh_W-RTA1E5EJa0fu9Zd759qLaT2rO2PLVgS4e2RGeZClk6SFUeq1qYxRGESW_WWb71sZwBd5DE6-lKGupvvg4WMkDjcu5LV9CLPBymE_aMKlRcvGAqg
```

The Auth0 Domain Name, JWT code signing secret and Auth0 Client ID are included in setup.sh


### Roles-based access control (RBAC)

There are three roles associated with this project:

* ADMIN: (all permissions)
  * username: adminwetfootfestival@gmail.com
  * password: #123Adminwetfootfestival
* VOLUNTEER: (all volunteer permissions)
  * username: volunteerwetfootfestival@gmail.com
  * password: #123Volunteerwetfootfestival
* ARTIST: (all artist permissions)
  * username: artistwetfootfestival@gmail.com
  * password: #123Artistwetfootfestival

You can use these to generate tokens if the provided ones are expired.

## API Documentation

There are the following endpoints availible:

### GET
#### /events

_Response:_
```
{'events': [{'artists': [{'email': 'gnarfunkelband@gmail.com', 'event': 1, 'id': 2, 'image_link': 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80', 'instagram_link': 'https://www.facebook.com/joeexotic', 'name': 'Gnarfunkel', 'phone_number': '555-555-5557', 'website': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}], 'email': 'wisehall@gmail.com', 'id': 1, 'name': 'Wetfoot Festival 2019', 'phone_number': '555-555-5555', 'theme': 'Major Tom Goes to Wonderland', 'venue_name': 'The Wisehall', 'volunteers': [{'email': 'annie@gmail.com', 'event': 1, 'id': 2, 'name': 'Annie', 'phone_number': '555-555-5559'}], 'website': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}], 'success': True}
```


#### /artists

_Response:_
```
{'artists': [{'email': 'gnarfunkelband@gmail.com', 'event': 1, 'id': 2, 'image_link': 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80', 'instagram_link': 'https://www.facebook.com/joeexotic', 'name': 'Gnarfunkel', 'phone_number': '555-555-5557', 'website': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}], 'success': True}
```

#### /volunteers

_Response:_
```
{'success': True, 'volunteers': [{'email': 'annie@gmail.com', 'event': 1, 'id': 2, 'name': 'Annie', 'phone_number': '555-555-5559'}]}
```

### POST
#### /events

_Response:_
```
{'events': {'artists': [], 'email': 'wise@gmail.com', 'id': 3, 'name': 'The MostWetFootFestival', 'phone_number': '778-777-5535', 'theme': 'Get schwifty!', 'venue_name': 'The wisest Hall', 'volunteers': [], 'website': 'www.google.com'}, 'success': True}
```

#### /artists

_Response:_
```
{'artists': {'email': 'maia@gmail.com', 'event': 1, 'id': 3, 'image_link': 'www.fakelink.com', 'instagram_link': 'www.instagram.com', 'name': 'Maia', 'phone_number': '778-777-5555', 'website': 'www.google.com'}, 'success': True}
```


#### /volunteers

_Response:_

```
{'success': True, 'volunteers': {'email': 'maia@gmail.com', 'event': 1, 'id': 3, 'name': 'Maia', 'phone_number': '778-777-5555'}}
```

### PATCH
#### /events

_Response:_
```
{'events': {'artists': [{'email': 'gnarfunkelband@gmail.com', 'event': 1, 'id': 2, 'image_link': 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80', 'instagram_link': 'https://www.facebook.com/joeexotic', 'name': 'The dopest band that ever doped', 'phone_number': '555-555-5557', 'website': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}], 'email': 'wisehall@gmail.com', 'id': 1, 'name': 'The Least WetFootFestival', 'phone_number': '555-555-5555', 'theme': 'Major Tom Goes to Wonderland', 'venue_name': 'The Wisehall', 'volunteers': [{'email': 'annie@gmail.com', 'event': 1, 'id': 2, 'name': 'Annie', 'phone_number': '555-555-5559'}], 'website': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}, 'success': True}
```

#### /artists

_Response:_

```
{'artists': {'email': 'gnarfunkelband@gmail.com', 'event': 1, 'id': 2, 'image_link': 'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80', 'instagram_link': 'https://www.facebook.com/joeexotic', 'name': 'The dopest band that ever doped', 'phone_number': '555-555-5557', 'website': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}, 'success': True}
```


#### /volunteers

_Response:_
```
{'success': True, 'volunteers': {'email': 'annie@gmail.com', 'event': 1, 'id': 2, 'name': 'Annie Bo Banie', 'phone_number': '778-777-5558'}}
```

### DELETE
#### /events

_Response:_
```
{'success': True}
```

#### /artists

_Response:_
```
{'success': True}
```

#### /volunteers

_Response:_
```
{'success': True}
```

## Deployment

`git push heroku master`

or

`make deploy`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License
MIT