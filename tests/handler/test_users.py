from tornado.testing import AsyncHTTPTestCase
from unittest.mock import patch
from main import make_app


class TestMetric(AsyncHTTPTestCase):
    @patch("main.MongoDb")
    def get_app(self, mock_mongo):
        self.mock = mock_mongo.return_value
        self.mock.find_all.return_value = {'_id': {'$oid': '1549759393502'}}
        return make_app()

    def test_should_return_ok_for_usual_scenario(self):
        response = self.fetch("/api/v1/users", method="GET")
        self.assertEqual(200, response.code)
