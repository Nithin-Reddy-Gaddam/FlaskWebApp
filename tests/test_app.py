import sys
import os
import unittest
from app import create_app
from models import db, User


# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class FlaskAppTestCase(unittest.TestCase):
    app = None

    @classmethod
    def setUpClass(cls):
        """Set up the test application"""
        cls.app = create_app()
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Destroy the test database"""
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        """Test if home page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """Test user registration"""
        response = self.client.post('/register', data={
            'username': 'tester',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        self.assertIn(b'Login', response.data)

    def test_login(self):
        """Test user login"""
        with self.app.app_context():
            user = User(username="tester", email="test@example.com", password="hashedpassword")
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        """Test if dashboard requires authentication"""
        response = self.client.get('/dashboard', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)


if __name__ == "__main__":
    unittest.main()
