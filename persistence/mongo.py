from logzero import logger
from pymongo import MongoClient
import settings

_client = None


class MongoDb:
    @classmethod
    def get_client(cls, new=False):

        global _client

        try:
            if new or not _client:
                _client = MongoClient(
                    username=settings.MONGO_USERNAME,
                    password=settings.MONGO_PASSWORD,
                    host=settings.MONGO_HOST,
                    port=int(settings.MONGO_PORT),
                    authSource='admin',
                    authMechanism='SCRAM-SHA-1'
                ).teste
        except Exception as err:
            logger.error(err)
            _client = None
        return _client

    @classmethod
    def users_collection(cls):
        collection = cls.get_client().users
        return collection
