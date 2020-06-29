import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Volunteer, Artist, Event


class WetfootFestivalTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'wetfootfestival_test'
        self.database_path = 'postgresql://{}/{}'.format(
            'localhost:5432', self.database_name)
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

    
    #---------------------------------------
    #           VOLUNTEER TESTS
    #---------------------------------------

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
        body = {
            'name': 'Maia',
            'phone_number': '778-777-5555',
            'email': 'maia@gmail.com',
            'event': 1
            }
        response = self.client().post("/volunteers",
                                      content_type="application/json",
                                      data=json.dumps(body))
        data = json.loads(response.data.decode())
        self.assertEqual(data["success"], True)
        self.assertEqual(response.status_code, 201)

    def test_patch_volunteer(self):
        """Test PATCH /volunteers"""
        new_name = 'Annie Bo Banie'
        new_phone = '778-777-5558'
        body = {
            'name': new_name,
            'phone_number': new_phone,
            }
        response = self.client().patch('/volunteers/2',
                                      content_type='application/json',
                                      data=json.dumps(body))
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(data['volunteers']['name'], new_name)
        self.assertEqual(data['volunteers']['phone_number'], new_phone)
        self.assertEqual(response.status_code, 200)

    def test_delete_volunteer(self):
        """Test DELETE /volunteers"""
        response = self.client().delete("/volunteers/1")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    
    #---------------------------------------
    #           ARTIST TESTS
    #---------------------------------------
    
    def test_get_artists(self):
        """Test GET /artists."""
        response = self.client().get("/artists")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertGreaterEqual(len(data['artists']), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_artist(self):
        """Test GET /artists/<int:event_id>."""
        response = self.client().get("/artists/2")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_post_artist(self):
        """Test POST /artists"""
        body = {
            'name': 'Maia',
            'phone_number': '778-777-5555',
            'email': 'maia@gmail.com',
            'event': 1,
            'website': 'www.google.com',
            'instagram_link': 'www.instagram.com',
            'image_link': 'www.fakelink.com'
            }
        response = self.client().post('/artists',
                                      content_type='application/json',
                                      data=json.dumps(body))
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 201)

    def test_patch_artist(self):
        """Test PATCH /artists"""
        new_name = 'The dopest band that ever doped'
        body = {
            'name': new_name,
            }
        response = self.client().patch('/artists/2',
                                      content_type='application/json',
                                      data=json.dumps(body))
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(data['artists']['name'], new_name)
        self.assertEqual(response.status_code, 200)

    def test_delete_artist(self):
        """Test DELETE /artists"""
        response = self.client().delete("/artists/1")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)


    #---------------------------------------
    #           EVENTS TESTS
    #---------------------------------------
    def test_get_events(self):
        """Test GET /events."""
        response = self.client().get("/events")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertGreaterEqual(len(data['events']), 1)
        self.assertEqual(response.status_code, 200)

    def test_get_event(self):
        """Test GET /events/<int:event_id>."""
        response = self.client().get("/events/1")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)

    def test_post_event(self):
        """Test POST /events"""
        body = {
            'name': 'The MostWetFootFestival',
            'phone_number': '778-777-5535',
            'email': 'wise@gmail.com',
            'website': 'www.google.com',
            'venue_name': 'The wisest Hall',
            'theme': 'Get schwifty!'
            }
        response = self.client().post('/events',
                                      content_type='application/json',
                                      data=json.dumps(body))
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 201)

    def test_patch_event(self):
        """Test PATCH /events"""
        new_name = 'The Least WetFootFestival'
        body = {
            'name': new_name,
            }
        response = self.client().patch('/events/1',
                                      content_type='application/json',
                                      data=json.dumps(body))
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], True)
        self.assertEqual(data['events']['name'], new_name)
        self.assertEqual(response.status_code, 200)

    # def test_delete_event(self):
    #     """Test DELETE /events"""
    #     response = self.client().delete("/events/1")
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(response.status_code, 200)

    #---------------------------------------
    #           ERROR HANDLING TESTS
    #---------------------------------------
    
    
    
    # def test_resource_not_found(self):
    #     """Test resource not found"""
    #     res = self.client().get("/fake-endpoint")
    #     self.assertEqual(res.status_code, 404)

    # def test_internal_service_error(self):
    #     """Test internal_service_error, should be rare"""
    #     response = self.client().get("/questions?page=3")
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(response.status_code, 500)

    # def unprocessible_entity_error(self):
    #     """Test unprocessible_entity_error"""
    #     body = {
    #         "question": "How many?",
    #         "answer": "5",
    #         "category": "not existant",  # needs an id, not a str.
    #         "difficulty": 5
    #     }
    #     response = self.client().post("/questions",
    #                                   content_type="application/json",
    #                                   data=json.dumps(body))
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(res.status_code, 422)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
