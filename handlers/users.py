import json

from handlers.base import BaseHandler
from marshmallow import ValidationError
from schemas.user import UserSchema
from util.error_throw import ErrorThrow
from persistence.mongo import MongoDb
from bson.json_util import dumps


class UsersHandler(BaseHandler):
    mongo = MongoDb()

    def get(self):
        try:
            result = self.mongo.users_collection().find()
        except Exception as err:
            print(err)
        else:
            response = list(json.loads(dumps(result)))
            self.set_status(200)
            self.finish({'code': self.get_status(), 'data': response})

    def post(self):
        request_body = json.loads(self.request.body)

        try:
            UserSchema().load(request_body)

        except ValidationError as err:
            raise ErrorThrow(reason=str(err), status_code=400)

        else:
            result = UserSchema().dumps(request_body)
            self.set_status(201)
            self.finish(result)
