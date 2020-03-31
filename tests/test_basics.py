import unittest
from flask import current_app
from app import create_app, db
from faker import Faker
from app.api.services import get_token, post_query
from app.api import utils


class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.fake = Faker()
        self.fake.seed_instance(103)
        self.email=current_app.config['EMAIL']
        self.password= current_app.config['PASSWORD']
        self.token_response = get_token(current_app.config['LOGIN_URL'], self.email, self.password)

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_get_token(self):

        status = self.token_response['status']

        self.assertEqual(status, "APPROVED", "status is approved")

    def test_report_request_with_valid_token(self):

        token = self.token_response['token']

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response = post_query(current_app.config['REPORT_URL'], token, data)

        status = response['status']

        self.assertEqual(status, "APPROVED", "status is not approved")

    def test_report_request_with_invalid_token(self):

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDddLCJ0aW1lc3RhbXAiOjE1ODU0MjgyOTF9.qlO2DtNL9FFGIitVWZySqWCuYq6EsoTPp0P0P_NT1wM"

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response = post_query(current_app.config['REPORT_URL'], token, data)

        status = response['status']

        self.assertEqual(status, "DECLINED", "status is not declined")

    def test_transaction_query_request(self):

        token = self.token_response['token']

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response = post_query(current_app.config['TRANSACTION_QUERY_URL'], token, data)

        per_page = response['per_page']

        self.assertEqual(per_page, 50, "per page is not found")

    def test_transaction(self):

        token = self.token_response['token']

        data = {"transactionId": "1011028-1539357144-1293"}

        response = post_query(current_app.config['TRANSACTION_URL'], token, data)

        customer_info = response['customerInfo']

        self.assertGreater(len(customer_info) , 0, "response should contain data")

    def test_client(self):

        token = self.token_response['token']

        data = {"transactionId": "1011028-1539357144-1293"}

        response = post_query(current_app.config['CLIENT_URL'], token, data)

        customer_info = response['customerInfo']

        self.assertGreater(len(customer_info), 0, "response should contain data")

    def test_report_request_for_object_conversion(self):

        token = self.token_response['token']

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response_data = post_query(current_app.config['REPORT_URL'], token, data)

        status = response_data['status']

        self.assertEqual(status, "APPROVED", "status is not approved")

        tmp_list = utils.convert_report_json_2_object_list(response_data['response'])

        self.assertGreater(len(tmp_list),0)

    def test_transaction_query_request_for_object_conversion(self):

        token = self.token_response['token']

        data = {"fromDate": "2000-01-01", "toDate": "2020-04-01"}

        response = post_query(current_app.config['TRANSACTION_QUERY_URL'], token, data)

        transaction_query_list = response['data']

        query_list = utils.convert_transaction_query_json_2_object_list(transaction_query_list)

        self.assertGreater(len(query_list), 0)


