# Wetfoot Festival

The Wetfoot Festival Website! Wetfoot festival is a festival that happens every year in Vancvouer, BC. This website allow for admins to create the festival every year and for artists and volunteers to sign up to contribute.

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


## Usage
Run the command below to start the app.

`make run`

## Unit tests

To run the unittest suit use:

`make test`

__NOTE:__ In order to run the test suit you need an active token from login in. This must then be put in the setup.sh file for ADMIN_TOKEN. For the purposes of testing, one has been provided.


## Running migrations
Use the following commands to run database migrations to add tables or columns.

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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhUUWJaTlZnYzVMVFVxdHFzU2t2YyJ9.eyJpc3MiOiJodHRwczovL3R5bGVycy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzM5NDcwMTI4MjUzNTgyNTk1OSIsImF1ZCI6IndldGZvb3RmZXN0aXZhbCIsImlhdCI6MTU5Mzc0MDU5MSwiZXhwIjoxNTkzNzQ3NzkxLCJhenAiOiJMRmxpbm40WUN5MkxObkpkenc2YzBrMnVPd2w1OW5LSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWZmZWN0OmFydGlzdHMiLCJhZmZlY3Q6ZXZlbnRzIiwiYWZmZWN0OnZvbHVudGVlcnMiXX0.X2ptB9VssyQGdK3IlVmsCMRUybRd6QdZmXrjgBTjaqBpuxO6ZO8AVt835OGiUfbA6GI5V_DClbK-AYYrJUf38xTuowAmvNkLNNLzT9xnrb1nlShkerqNwZeJnpuRd0bBN0BzaYpI0vRVNekTUJw0NalazDvf2ktFRyy-VSRcUfRo1oxHft8XTnu9Wn3I30ps_EiCV07nOM-TnDMBKTiAH6rT5UMOTL05oQslzl2F2Q2GRh7NmuDvJd89KWJ_V7XUtXV6_XEETp8BnpDTEfDfrOLBUM1tpVnqdqGkepo05pvUA4y6932IqBjmoJMxiCNRTrQ230GMycsf1v1EAa7CRw
```

The Auth0 Domain Name, JWT code signing secret and Auth0 Client ID are included in setup.sh

## Signing in

visit `https://wetfootfestival.herokuapp.com/login`.

This will get you a token with no roles assigned that can currently communicate with the `GET` endpoints.

## roles-based access control (RBAC)

There are three roles associated with this project:

* ADMIN: `affect:events`, `affect:artists`, `affect:volunteers`
* VOLUNTEER: `affect:volunteers`
* ARTIST: `affect:artists`


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


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

License
