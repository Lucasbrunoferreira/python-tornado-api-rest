from handlers.base import BaseHandler
from marshmallow import ValidationError
from schemas.user import UserSchema
from util.error_throw import ErrorThrow
from persistence.mongo import MongoDb
from bson.json_util import dumps
from logzero import logger
from util import data_formatter


import json


class UsersHandler(BaseHandler):
    mongo = MongoDb()

    def get(self):
        try:
            result = self.mongo.users_collection().find()
        except Exception as err:
            logger.error('error in find users', err)
            raise ErrorThrow(status_code=500, reason=str(err))
        else:
            response = list(json.loads(dumps(result)))

            formatted_response = data_formatter.object_id_and_timestamp('created_at', response)

            self.write_response(status_code=200, result=formatted_response)

    def post(self):
        request_body = json.loads(self.request.body)

        try:
            new_user = UserSchema().load(request_body)

        except ValidationError as err:
            logger.error('error in validate user schema', err)
            raise ErrorThrow(status_code=400, reason=str(err))

        else:
            try:
                response = self.mongo.users_collection().insert_one(new_user)
            except Exception as err:
                logger.error('error in save user in database', err)
                raise ErrorThrow(status_code=400, reason=str(err))
            else:
                self.write_response(status_code=201, result=str(response.inserted_id))
