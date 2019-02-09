from handlers.base import BaseHandler
from marshmallow import ValidationError
from persistence.schemas.user import UserSchema
from util.error_throw import ErrorThrow
from persistence.database.mongo import MongoDb
from logzero import logger
from util import data_formatter

import json


class UsersHandler(BaseHandler):
    mongo = MongoDb(collection='users')

    def get(self):
        try:
            result = self.mongo.find_all()

        except Exception as err:
            logger.error('error in find users', err)
            raise ErrorThrow(status_code=500, reason=str(err))

        else:
            formatted_response = data_formatter.object_id_and_timestamp('created_at', result)
            self.write_response(status_code=200, result=formatted_response)

    def post(self):
        request_body = json.loads(self.request.body)

        try:
            new_user = UserSchema().load(request_body)

        except ValidationError as err:
            logger.error('error in validate user schema {}'.format(err))
            raise ErrorThrow(status_code=400, reason=str(err))

        else:
            try:
                response = self.mongo.insert_one(new_user)

            except Exception as ex:
                print(ex)
                logger.error('error in save user in database {}'.format(ex))
                raise ErrorThrow(status_code=400, reason=str(ex))

            else:
                self.write_response(status_code=201, result=response)
