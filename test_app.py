from app import create_app
import os
import unittest
import json
from mock import patch
from auth.auth import requires_auth
from functools import wraps
from flask_sqlalchemy import SQLAlchemy


from models import setup_db, Volunteer, Artist, Event
import os

ADMIN_TOKEN = os.environ['ADMIN_TOKEN']
ARTIST_TOKEN = os.environ['ARTIST_TOKEN']
VOLUNTEER_TOKEN = os.environ['VOLUNTEER_TOKEN']


def mock_decorator():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
        return decorated_function
    return decorator


# Auth patch mock decorator https://stackoverflow.com/questions/47900727/mock-authentication-decorator-in-unittesting


class WetfootFestivalTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        patch('auth.auth.requires_auth', mock_decorator).start()
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client
        self.database_name = 'wetfootfestival'
        self.database_path = 'postgresql://{}/{}'.format(
            'localhost:5432', self.database_name)
        self.new_event = {
            'name': 'The MostWetFootFestival',
            'phone_number': '778-777-5535',
            'email': 'wise@gmail.com',
            'website': 'www.google.com',
            'venue_name': 'The wisest Hall',
            'theme': 'Get schwifty!'
        }
        self.new_volunteer = {
            'name': 'Maia',
            'phone_number': '778-777-5555',
            'email': 'maia_volunteer@gmail.com',
            'event': 1
        }

        self.new_artist = {
            'name': 'Maia',
            'phone_number': '778-777-5555',
            'email': 'maia_artist@gmail.com',
            'event': 1,
            'website': 'www.google.com',
            'instagram_link': 'www.instagram.com',
            'image_link': 'www.fakelink.com'
        }

        self.auth_header_admin = {
            "Authorization": "Bearer {}".format(ADMIN_TOKEN)}
        self.auth_header_artist = {
            "Authorization": "Bearer {}".format(ARTIST_TOKEN)}
        self.auth_header_volunteer = {
            "Authorization": "Bearer {}".format(VOLUNTEER_TOKEN)}
        self.auth_header_bad = {
            "Authorization": "{}".format(ADMIN_TOKEN)}

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_get_status(self):
        """Test GET /status/am-i-up"""
        response = self.client().get('/status/am-i-up')
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    # #---------------------------------------
    # #           VOLUNTEER TESTS
    # #---------------------------------------

    def test_get_volunteers(self):
        """Test GET /volunteers."""
        response = self.client().get('/volunteers')
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertGreaterEqual(len(data['volunteers']), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_volunteer(self):
        """Test GET /volunteers/<int:volunteer_id>."""
        response = self.client().get('/volunteers/2')
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_post_volunteer(self):
        """Test POST /volunteers"""
        response = self.client().post("/volunteers",
                                      content_type="application/json",
                                      headers=self.auth_header_admin,
                                      data=json.dumps(self.new_volunteer))
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual(data["success"], True)
        self.assertEqual(response.status_code, 201)

    # def test_patch_volunteer(self):
    #     """Test PATCH /volunteers"""
    #     new_name = 'Annie Bo Banie'
    #     new_phone = '778-777-5558'
    #     body = {
    #         'name': new_name,
    #         'phone_number': new_phone,
    #     }
    #     response = self.client().patch('/volunteers/2',
    #                                    content_type='application/json',
    #                                    headers=self.auth_header_admin,
    #                                    data=json.dumps(body))
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['volunteers']['name'], new_name)
    #     self.assertEqual(data['volunteers']['phone_number'], new_phone)
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_volunteer(self):
    #     """Test DELETE /volunteers"""
    #     response = self.client().delete("/volunteers/1",
    #                                     headers=self.auth_header_admin)
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)

    # # #---------------------------------------
    # # #           ARTIST TESTS
    # # #---------------------------------------

    # def test_get_artists(self):
    #     """Test GET /artists."""
    #     response = self.client().get("/artists")
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertGreaterEqual(len(data['artists']), 1)
    #     self.assertEqual(response.status_code, 200)

    # def test_get_artist(self):
    #     """Test GET /artists/<int:event_id>."""
    #     response = self.client().get("/artists/2")
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)

    # def test_post_artist(self):
    #     """Test POST /artists"""
    #     response = self.client().post('/artists',
    #                                   content_type='application/json',
    #                                   headers=self.auth_header_admin,
    #                                   data=json.dumps(self.new_artist))
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 201)

    # def test_patch_artist(self):
    #     """Test PATCH /artists"""
    #     new_name = 'The dopest band that ever doped'
    #     body = {
    #         'name': new_name,
    #     }
    #     response = self.client().patch('/artists/2',
    #                                    content_type='application/json',
    #                                    headers=self.auth_header_admin,
    #                                    data=json.dumps(body))
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['artists']['name'], new_name)
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_artist(self):
    #     """Test DELETE /artists"""
    #     response = self.client().delete("/artists/1",
    #                                     headers=self.auth_header_admin)
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)

    # # #---------------------------------------
    # # #           EVENTS TESTS
    # # #---------------------------------------

    # def test_get_events(self):
    #     """Test GET /events."""
    #     response = self.client().get("/events")
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertGreaterEqual(len(data['events']), 1)
    #     self.assertEqual(response.status_code, 200)

    # def test_get_event(self):
    #     """Test GET /events/<int:event_id>."""
    #     response = self.client().get("/events/1")
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)

    # def test_post_event(self):
    #     """Test POST /events"""
    #     response = self.client().post('/events',
    #                                   content_type='application/json',
    #                                   headers=self.auth_header_admin,
    #                                   data=json.dumps(self.new_event))
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 201)

    # def test_patch_event(self):
    #     """Test PATCH /events"""
    #     new_name = 'The Least WetFootFestival'
    #     body = {
    #         'name': new_name,
    #     }
    #     response = self.client().patch('/events/1',
    #                                    content_type='application/json',
    #                                    headers=self.auth_header_admin,
    #                                    data=json.dumps(body))
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['events']['name'], new_name)
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_event(self):
    #     """Test DELETE /events"""
    #     response = self.client().delete("/events/2",
    #                                     headers=self.auth_header_admin)
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)

    # # ---------------------------------------
    # #           ERROR HANDLING TESTS
    # # ---------------------------------------

    # def test_resource_not_found(self):
    #     """Test resource not found"""
    #     res = self.client().get("/fake-endpoint")
    #     self.assertEqual(res.status_code, 404)

    # def test_internal_service_error(self):
    #     """Test internal_service_error, should be rare"""
    #     response = self.client().delete("/events/10",
    #                                     headers=self.auth_header_admin)
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(response.status_code, 500)

    # def unprocessible_entity_error(self):
    #     """Test unprocessible_entity_error"""
    #     body = {"thisShould": "fail"}
    #     response = self.client().post("/events/10",
    #                                   content_type="application/json",
    #                                   headers=self.auth_header_admin,
    #                                   data=json.dumps(body))
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(res.status_code, 422)

    # # ---------------------------------------
    # #           RBAC TESTS
    # # ---------------------------------------

    # def test_add_artist_admin(self):
    #     newer_artist = {
    #         'name': 'Maia2',
    #         'phone_number': '778-777-55552',
    #         'email': 'maia2@gmail.com',
    #         'event': 1,
    #         'website': 'www.google2.com',
    #         'instagram_link': 'www.instagram2.com',
    #         'image_link': 'www.fakelink2.com'
    #     }
    #     res = self.client().post('/artists',
    #                              headers=self.auth_header_admin,
    #                              json=newer_artist)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 201)

    # def test_bad_add_event_admin(self):
    #     res = self.client().post('/events',
    #                              headers=self.auth_header_bad,
    #                              json=self.new_event)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 401)

    # def test_add_artist_artist(self):

    #     new_artist = {
    #         'name': 'Maia3',
    #         'phone_number': '778-777-55553',
    #         'email': 'maia54@gmail.com',
    #         'event': 1,
    #         'website': 'www.google3.com',
    #         'instagram_link': 'www.instagram3.com',
    #         'image_link': 'www.fakelink3.com'
    #     }
    #     res = self.client().post('/artists',
    #                              headers=self.auth_header_artist,
    #                              json=new_artist)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 201)

    # def test_add_event_artist(self):
    #     res = self.client().post('/events',
    #                              headers=self.auth_header_bad,
    #                              json=self.new_event)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 401)

    # def test_add_artist_volunteer(self):

    #     new_volunteer = {
    #         'name': 'Maia2',
    #         'phone_number': '778-777-55',
    #         'email': 'maia_volunteer2@gmail.com',
    #         'event': 1
    #     }

    #     res = self.client().post('/volunteers',
    #                              headers=self.auth_header_volunteer,
    #                              json=new_volunteer)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 201)

    # def test_add_event_volunteer(self):
    #     res = self.client().post('/events',
    #                              headers=self.auth_header_bad,
    #                              json=self.new_event)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
