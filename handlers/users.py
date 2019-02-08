import json

from handlers.base import BaseHandler
from marshmallow import ValidationError
from schemas.user import UserSchema
from util.error_throw import ErrorThrow
from persistence.mongo import MongoDb
from bson.json_util import dumps
from logzero import logger
from util.remove_object_id import remove_objectid

class UsersHandler(BaseHandler):
    mongo = MongoDb()

    def get(self):
        try:
            result = self.mongo.users_collection().find()
        except Exception as err:
            logger.error('error in find users', err)
            raise ErrorThrow(reason=str(err), status_code=500)
        else:
            response = list(json.loads(dumps(result)))

            self.set_status(200)
            self.finish({'code': self.get_status(), 'data': remove_objectid(response)})

    def post(self):
        request_body = json.loads(self.request.body)
        try:
            UserSchema().load(request_body)

        except ValidationError as err:
            logger.error('error in validate user schema', err)
            raise ErrorThrow(reason=str(err), status_code=400)

        else:
            new_user = dict(json.loads(UserSchema().dumps(request_body)))

            try:
                response = self.mongo.users_collection().insert_one(new_user)
            except Exception as err:
                logger.error('error in save user in database', err)
                raise ErrorThrow(reason=str(err), status_code=400)
            else:
                self.set_status(201)

                self.finish({'code': self.get_status(), 'data':  str(response.inserted_id)})
