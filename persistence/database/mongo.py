from logzero import logger
from pymongo import MongoClient
from bson.json_util import dumps, ObjectId

import settings
import json

_client_database = None


class MongoDb:
    def __init__(self, collection):
        self.collection = self.mongo_client_database()[collection]

    @classmethod
    def mongo_client_database(cls, new=False):
        global _client_database

        try:
            if new or not _client_database:
                _client_database = MongoClient(settings.MONGO_URI)

        except Exception as err:
            logger.error(err)
            _client_database = None
        return _client_database.get_database()

    def insert_one(self, data: dict):
        try:
            response = self.collection.insert_one(data, return_document=True)

        except Exception as ex:
            raise ex
        else:
            return str(response.inserted_id)

    def find_all(self):
        try:
            response = self.collection.find()
        except Exception as ex:
            raise ex
        else:
            return list(json.loads(dumps(response)))

    def find_one(self, document_id: str):
        try:
            response = self.collection.find_one({'_id': ObjectId(document_id)})
        except Exception as ex:
            raise ex
        else:
            if response is not None:
                return dict(json.loads(dumps(response)))
            else:
                raise ValueError

    def update_one(self, document_id, document):
        try:
            response = self.collection.find_one_and_update(
                {'_id': ObjectId(document_id)},
                {'$set': document},
                return_document=True)
        except Exception as ex:
            raise ex
        else:
            if response is None:
                raise ValueError
            else:
                return dict(json.loads(dumps(response)))

    def delete_one(self, document_id):
        try:
            response = self.collection.find_one_and_delete({'_id': ObjectId(document_id)})
        except Exception as ex:
            raise ex
        else:
            if response is None:
                raise ValueError
            else:
                pass
