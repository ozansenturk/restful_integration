import unittest
from flask import current_app
from app import create_app, db
from faker import Faker
from app.api.utils import get_token, post_query

class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.fake = Faker()
        self.fake.seed_instance(103)

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_get_token(self):

        login_url = "/merchant/user/login"

        email = "demo@financialhouse.io"
        password = "cjaiU8CV"

        token_response = get_token(login_url, email, password)

        status = token_response['status']

        self.assertEqual(status, "APPROVED", "status is approved")

    def test_report_request_with_valid_token(self):

        login_url = "/merchant/user/login"
        report_url = "/transactions/report"

        email = "demo@financialhouse.io"
        password = "cjaiU8CV"

        token_response = get_token(login_url, email, password)

        token = token_response['token']

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response = post_query(report_url, token, data)

        status = response['status']

        self.assertEqual(status, "APPROVED", "status is not approved")


    def test_report_request_with_invalid_token(self):

        login_url = "/merchant/user/login"
        report_url = "/transactions/report"

        email = "demo@financialhouse.io"
        password = "cjaiU8CV"

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDddLCJ0aW1lc3RhbXAiOjE1ODU0MjgyOTF9.qlO2DtNL9FFGIitVWZySqWCuYq6EsoTPp0P0P_NT1wM"

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response = post_query(report_url, token, data)

        status = response['status']

        self.assertEqual(status, "DECLINED", "status is not declined")

    def test_transaction_query_request(self):

        login_url = "/merchant/user/login"
        transaction_query_url = "/transaction/list"

        email = "demo@financialhouse.io"
        password = "cjaiU8CV"

        token_response = get_token(login_url, email, password)

        token = token_response['token']

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response = post_query(transaction_query_url, token, data)

        status = response['status']

        self.assertEqual(status, "APPROVED", "status is not approved")

    def test_transaction(self):

        login_url = "/merchant/user/login"
        transaction_url = "/transaction"

        email = "demo@financialhouse.io"
        password = "cjaiU8CV"

        token_response = get_token(login_url, email, password)

        token = token_response['token']

        data = {"transactionId": "1011028-1539357144-1293"}

        response = post_query(transaction_url, token, data)

        customerInfo = response['customerInfo']

        self.assertGreater(len(customerInfo) , 0, "response should contain data")

    def test_client(self):
        login_url = "/merchant/user/login"
        client_url = "/client"

        email = "demo@financialhouse.io"
        password = "cjaiU8CV"

        token_response = get_token(login_url, email, password)

        token = token_response['token']

        data = {"transactionId": "1011028-1539357144-1293"}

        response = post_query(client_url, token, data)

        customerInfo = response['customerInfo']

        self.assertGreater(len(customerInfo), 0, "response should contain data")