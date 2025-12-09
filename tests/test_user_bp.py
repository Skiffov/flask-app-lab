import unittest
from app import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_greetings_page(self):
        response = self.client.get("/users/hi/Peter?age=18")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Peter", response.data)

    def test_admin_page(self):
        response = self.client.get("/users/admin")
        self.assertEqual(response.status_code, 302)
