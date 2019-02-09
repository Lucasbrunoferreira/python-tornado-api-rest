from logzero import logger
from pymongo import MongoClient
from bson.json_util import dumps

import settings
import json

_client = None


class MongoDb:
    def __init__(self, collection):
        self.collection = self.mongo_client()[collection]

    @classmethod
    def mongo_client(cls, new=False):
        global _client

        try:
            if new or not _client:
                _client = MongoClient(settings.MONGO_URI).teste

        except Exception as err:
            logger.error(err)
            _client = None

        return _client

    def insert_one(self, data: dict):
        try:
            response = self.collection.insert_one(data)

        except Exception as ex:
            logger.exception(ex)
            raise ex

        else:
            return str(response.inserted_id)

    def find_all(self):
        try:
            response = self.collection.find()

        except Exception as ex:
            raise ex

        else:
            result = list(json.loads(dumps(response)))
            return result
