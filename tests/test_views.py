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

    def test_transaction_query_page(self):
        response = self.client.get('/transaction_query/2')
        self.assertEqual(response.status_code, 200)
        # self.app.logger.debug("response.data {}".format(response.data))
        self.assertTrue(b'Tenants within 25 years listed' in response.data)
