import os
from flask import Flask, request, jsonify, abort, redirect
from models import setup_db, Volunteer, Artist, Event
from flask_cors import CORS
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/status/am-i-up', methods=['GET'])
    def am_i_up():
        """Check to see if the app is running

        Returns:
            response, code -- the response and code
        """
        response = jsonify({
            'success': True,
        })

        return response, 200

    @app.route('/login-results', methods=['GET'])
    def login_results():
        """The result of the login

        Returns:
            response: json, status code
        """
        response = jsonify({
            'greeting': "hello there!"
        })
        return response, 200

    @app.route('/login', methods=['GET'])
    def login():
        """The login

        Returns:
            response: json, status code
        """
        domain = "tylers-test.auth0.com"
        audience = "wetfootfestival"
        client_id = "LFlinn4YCy2LNnJdzw6c0k2uOwl59nKH"
        redirect_uri = "https://wetfootfestival.herokuapp.com/login-results"
        auth0_login = f"https://{domain}/authorize?audience={audience}}&response_type=token&client_id={client_id}&redirect_uri={redirect_uri}"
        print(auth0_login)
        return redirect(auth0_login)


    #---------------------------------------
    #           VOLUNTEER CONTROLLERS
    #---------------------------------------
    @app.route('/volunteers/<int:volunteer_id>', methods=['GET'])
    def get_volunteer(volunteer_id):
        """Gets a single volunteer

        Args:
            volunteer_id (int): The volunteer id e.g "1"

        Returns:
            response: json, status code
        """
        try:
            volunteer = Volunteer.query.filter_by(id=volunteer_id).one_or_none()
            response = jsonify({
                'volunteers': volunteer.format(),
                'success': True
            })
            return response, 200
        except Exception as e:
            app.logger.error(e)
            abort(404)


    @app.route('/volunteers', methods=['GET'])
    def get_volunteers():
        """Gets all of the volunteers in the database

        Returns:
            response: json, status code
        """
        try:
            response = jsonify({
                'volunteers': [volunteer.format() for volunteer in Volunteer.query.all()],
                'success': True
            })
            return response, 200
        except Exception as e:
            app.logger.error(e)
            abort(500)

    @app.route('/volunteers', methods=['POST'])
    def create_volunteer():
        """Creates a Volunteer.

        Returns:
            response: json, status_code
        """
        try:
            body = request.get_json()
            volunteer = Volunteer(
                name=body.get('name'),
                phone_number=body.get('phone_number'),
                email=body.get('email'),
                event=body.get('event'),
            )
            volunteer.insert()
            return jsonify({
                'success': True,
                'volunteers': volunteer.format()
            }), 201
        except Exception as e:
            app.logger.error(e)
            abort(422)

    @app.route('/volunteers/<int:volunteer_id>', methods=['PATCH'])
    def update_volunteer(volunteer_id):
        """Updates a volunteer

        Args:
            volunteer_id (int): the volunteer id to update

        Returns:
            response: json, status_code
        """
        try:
            body = request.get_json()
            volunteer = Volunteer.query.filter_by(id=volunteer_id).one_or_none()

            volunteer.name = body.get('name', volunteer.name)
            volunteer.phone_number = body.get('phone_number', volunteer.phone_number)
            volunteer.email = body.get('email', volunteer.email)
            volunteer.event = body.get('event', volunteer.event)

            return jsonify({
                'success': True,
                'volunteers': volunteer.format()
            }), 200
        except Exception as e:
            app.logger.error(e)
            abort(422)

    @app.route('/volunteers/<int:volunteer_id>', methods=['DELETE'])
    def delete_volunteer(volunteer_id):
        try:
            volunteer = Volunteer.query.filter_by(id=volunteer_id).one_or_none()
            volunteer.delete()
            return jsonify({
                'success': True,
            }), 200
        except Exception as e:
            app.logger.error(e)
            abort(500)
    
    
    #---------------------------------------
    #           ARTIST CONTROLLERS
    #---------------------------------------

    @app.route('/artists/<int:artist_id>', methods=['GET'])
    def get_artist(artist_id):
        """Gets a single artist

        Args:
            artists_id ([type]): The artist id e.g "1"

        Returns:
            response: json, status code
        """
        try:
            artist = Artist.query.filter_by(id=artist_id).one_or_none()
            response = jsonify({
                'artists': artist.format(),
                'success': True
            })
            return response, 200
        except Exception as e:
            app.logger.error(e)
            abort(404)


    @app.route('/artists', methods=['GET'])
    def get_artists():
        """Gets all of the artists in the database

        Returns:
            response: json, status code
        """
        try:
            response = jsonify({
                'artists': [artist.format() for artist in Artist.query.all()],
                'success': True
            })
            return response, 200
        except Exception as e:
            app.logger.error(e)
            abort(500)

    @app.route('/artists', methods=['POST'])
    def create_artist():
        """Creates a Artist.

        Returns:
            response: json, status_code
        """
        try:
            body = request.get_json()
            artist = Artist(
                name=body.get('name'),
                phone_number=body.get('phone_number'),
                email=body.get('email'),
                event=body.get('event'),
                website=body.get('website'),
                instagram_link=body.get('instagram_link'),
                image_link=body.get('image_link')
            )
            artist.insert()
            return jsonify({
                "success": True,
                "artists": artist.format()
            }), 201
        except Exception as e:
            app.logger.error(e)
            abort(422)

    @app.route('/artists/<int:artist_id>', methods=['PATCH'])
    def update_artist(artist_id):
        """Updates a artists

        Args:
            artists_id (int): the artists id to update

        Returns:
            response: json, status_code
        """
        try:
            body = request.get_json()
            artist = Artist.query.filter_by(id=artist_id).one_or_none()

            artist.name = body.get('name', artist.name)
            artist.phone_number = body.get('phone_number', artist.phone_number)
            artist.email = body.get('email', artist.email)
            artist.event = body.get('event', artist.event)
            artist.website = body.get('website', artist.website)
            artist.instagram_link = body.get('instagram_link', artist.instagram_link)
            artist.image_link = body.get('image_link', artist.image_link)
            artist.update()
            
            return jsonify({
                'success': True,
                'artists': artist.format()
            }), 200
        except Exception as e:
            app.logger.error(e)
            abort(422)

    @app.route('/artists/<int:artist_id>', methods=['DELETE'])
    def delete_artists(artist_id):
        try:
            artists = Artist.query.filter_by(id=artist_id).one_or_none()
            artists.delete()
            return jsonify({
                'success': True,
            }), 200
        except Exception as e:
            app.logger.error(e)
            abort(500)

    #---------------------------------------
    #           EVENT CONTROLLERS
    #---------------------------------------

    @app.route('/events/<int:event_id>', methods=['GET'])
    def get_event(event_id):
        """Gets a single event

        Args:
            event_id (int): The event id e.g "1"

        Returns:
            response: json, status code
        """
        try:
            event = Event.query.filter_by(id=event_id).one_or_none()
            response = jsonify({
                'events': event.format(),
                'success': True
            })
            return response, 200
        except Exception as e:
            app.logger.error(e)
            abort(404)


    @app.route('/events', methods=['GET'])
    def get_events():
        """Gets all of the events in the database

        Returns:
            response: json, status code
        """
        try:
            response = jsonify({
                'events': [event.format() for event in Event.query.all()],
                'success': True
            })
            return response, 200
        except Exception as e:
            app.logger.error(e)
            abort(500)

    @app.route('/events', methods=['POST'])
    def create_event():
        """Creates a Event.

        Returns:
            response: json, status_code
        """
        try:
            body = request.get_json()
            event = Event(
                name=body.get('name'),
                phone_number=body.get('phone_number'),
                email=body.get('email'),
                venue_name=body.get('venue_name'),
                theme=body.get('theme'),
                website=body.get('website')
            )
            event.insert()
            return jsonify({
                'success': True,
                'events': event.format()
            }), 201
        except Exception as e:
            app.logger.error(e)
            abort(422)

    @app.route('/events/<int:event_id>', methods=['PATCH'])
    def update_event(event_id):
        """Updates an event

        Args:
            event_id (int): the event id to update

        Returns:
            response: json, status_code
        """
        try:
            body = request.get_json()
            event = Event.query.filter_by(id=event_id).one_or_none()

            event.name = body.get('name', event.name)
            event.phone_number = body.get('phone_number', event.phone_number)
            event.email = body.get('email', event.email)
            event.venue_name = body.get('event', event.venue_name)
            event.theme = body.get('theme', event.theme)
            event.update()
            return jsonify({
                'success': True,
                'events': event.format()
            }), 200
        except Exception as e:
            app.logger.error(e)
            abort(422)

    @app.route('/events/<int:event_id>', methods=['DELETE'])
    def delete_event(event_id):
        """Deletes an event

        Returns:
            response: json, status_code
        """
        #TODO: How to handle the artist and volunteer entries?
        try:
            event = Event.query.filter_by(id=event_id).one_or_none()
            event.delete()
            return jsonify({
                'success': True,
            }), 200
        except Exception as e:
            app.logger.error(e)
            abort(500)


    #---------------------------------------
    #           ERROR HANDLERS
    #---------------------------------------

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422


    @app.errorhandler(404)
    def resource_not_found_error(error):
        response = jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        })
        return response, 404


    @app.errorhandler(AuthError)
    def unprocessible_entity_error(error):
        response = jsonify({
            'success': False,
            'error': error.status_code,
            'message': 'AuthError: {}'.format(error.error)
        })
        return response, error.status_code


    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify({
            'success': False,
            'message': 'There was an internal service error: {}'.format(error)
        })
        return response, 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run()