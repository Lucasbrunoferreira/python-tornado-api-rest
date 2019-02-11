from logzero import logger
from pymongo import MongoClient
from bson.json_util import dumps, ObjectId

import settings
import json

_mongo_client = None


class MongoDb:
    database_collection: None

    def __init__(self):
        self.get_mongo_client()

    def get_mongo_client(self, new=False):
        global _mongo_client

        try:
            if new or not _mongo_client:
                _mongo_client = MongoClient(settings.MONGO_URI)
                self.database_collection = _mongo_client.get_database()
        except Exception as err:
            logger.error(err)
            _mongo_client = None
        return _mongo_client

    def define_collection(self, collection):
        self.database_collection = self.database_collection[collection]

    def insert_one(self, data: dict):
        try:
            response = self.database_collection.insert_one(data)

        except Exception as ex:
            raise ex
        else:
            return str(response.inserted_id)

    def find_all(self):
        try:
            response = self.database_collection.find()
        except Exception as ex:
            raise ex
        else:
            return list(json.loads(dumps(response)))

    def find_one(self, document_id: str):
        try:
            response = self.database_collection.find_one({'_id': ObjectId(document_id)})
        except Exception as ex:
            raise ex
        else:
            if response is not None:
                return dict(json.loads(dumps(response)))
            else:
                raise ValueError

    def update_one(self, document_id, document):
        try:
            response = self.database_collection.find_one_and_update(
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
            response = self.database_collection.find_one_and_delete({'_id': ObjectId(document_id)})
        except Exception as ex:
            raise ex
        else:
            if response is None:
                raise ValueError
            else:
                pass
