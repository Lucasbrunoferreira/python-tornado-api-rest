from tornado.testing import AsyncHTTPTestCase
from unittest.mock import patch
from main import make_app


class TestUsers(AsyncHTTPTestCase):
    request_body = b'{"name": "Teste Python", "email": "email@teste.com"}'

    @patch("main.MongoDb")
    def get_app(self, mock_mongo=None):
        self.mock = mock_mongo.return_value
        self.mock.find_all.return_value = \
            self.mock.find_one.return_value = \
            self.mock.update_one.return_value \
            = {'_id': {'$oid': '1549759393502'}}
        return make_app()

    def test_should_return_ok_for_get_all(self):
        response = self.fetch("/api/v1/users", method="GET")
        self.assertEqual(200, response.code)

    def test_should_return_ok_for_post_new_user(self):
        response = self.fetch("/api/v1/users", method="POST", body=self.request_body)
        self.assertEqual(201, response.code)

    def test_should_return_bad_request_for_bad_email(self):
        body = b'{"name": "Teste Python", "email": "bademail"}'
        response = self.fetch("/api/v1/users", method="POST", body=body)
        self.assertEqual(400, response.code)

    def test_should_return_ok_for_edit_user(self):
        response = self.fetch("/api/v1/users/1549759393502", method="PUT", body=self.request_body)
        self.assertEqual(200, response.code)

    def test_should_return_ok_for_delete(self):
        response = self.fetch("/api/v1/users/1549759393502", method="DELETE")
        self.assertEqual(200, response.code)
