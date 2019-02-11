import unittest
from util import data_formatter


class TestDataFormatter(unittest.TestCase):
    objectid = '5c5f8fd49d885530a10743e'
    timestamp = '1549759393502'

    def test_formatter_object_id_in_dict(self):
        data = {'_id': {'$oid': self.objectid}}
        result = data_formatter.object_id(data)
        self.assertEqual(result, {'id': self.objectid})

    def test_formatter_object_id_in_list(self):
        data = [{'_id': {'$oid': self.objectid}}]
        result = data_formatter.object_id(data)
        self.assertEqual(result, [{'id': self.objectid}])

    def test_formatter_object_id__if_is_string(self):
        self.assertRaises(TypeError, data_formatter.object_id, self.objectid)

    def test_formatter_object_id_in_incomplete_dict(self):
        self.assertRaises(ValueError, data_formatter.object_id, {'_id': self.objectid})

    def test_formatter_object_id_in_empty_list(self):
        result = data_formatter.object_id([])
        self.assertEqual([], result)

    def test_formatter_timestamp_in_dict(self):
        data = {'date': {'$date': self.timestamp}}
        result = data_formatter.timestamp(key='date', data=data)
        self.assertEqual(result, {'date': '2019-02-10 00:43:13'})

    def test_formatter_timestamp_in_list(self):
        data = [{'date': {'$date': self.timestamp}}]
        result = data_formatter.timestamp(key='date', data=data)
        self.assertEqual(result, [{'date': '2019-02-10 00:43:13'}])

    def test_formatter_timestamp_is_string(self):
        self.assertRaises(TypeError, data_formatter.timestamp, self.timestamp)

    def test_formatter_timestamp_in_empty_list(self):
        result = data_formatter.timestamp(key='date', data=[])
        self.assertEqual([], result)

    def test_formatter_timestamp_not_contains_key(self):
        result = data_formatter.timestamp(key='date', data={'name': 'lucas'})
        self.assertEqual({'name': 'lucas'}, result)
