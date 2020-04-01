import re
import io
import unittest
from app import create_app, fake
from flask import url_for

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_transaction_page(self):
        response = self.client.post('/transaction')
        self.assertEqual(response.status_code, 200)

