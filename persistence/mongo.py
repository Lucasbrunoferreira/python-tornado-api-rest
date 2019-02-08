from pymongo import MongoClient


class MongoDb:
    DB_NAME = 'teste'
    DB_HOST = '127.0.0.1'
    DB_PORT = 8080
    DB_USER = 'admin'
    DB_PASS = 'admin'
    connection = MongoClient(DB_HOST, DB_PORT)

    def __init__(self):
        self.connection['admin'].authenticate(self.DB_USER, self.DB_PASS)

    def users_collection(self):
        database = self.connection[self.DB_NAME]
        return database['users']
