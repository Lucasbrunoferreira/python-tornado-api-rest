from handlers.base import BaseHandler
from marshmallow import ValidationError
from persistence.schemas.user import UserSchema
from util.error_throw import ErrorThrow
from logzero import logger
from util import data_formatter
from http import HTTPStatus

import json


class UsersHandler(BaseHandler):

    def prepare(self):
        self.settings['mongo'].define_collection('users')
        pass

    def data_received(self, chunk=None):
        if self.request.body:
            return json.loads(self.request.body)

    def get(self, key):
        try:
            if not key:
                result = self.settings['mongo'].find_all()
            else:
                result = self.settings['mongo'].find_one(key)
        except ValueError:
            raise ErrorThrow(status_code=HTTPStatus.BAD_REQUEST,
                             reason='no user found with id {}'.format(key))
        except Exception as err:
            logger.error(err)
            raise ErrorThrow(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                             reason=str(err))
        else:
            formatted_response = data_formatter.object_id_and_timestamp('created_at', result)
            self.write_response(status_code=HTTPStatus.OK,
                                result=formatted_response)

    def post(self, key):
        try:
            new_user = UserSchema().load(self.data_received())
        except ValidationError as err:
            logger.error(err)
            raise ErrorThrow(status_code=HTTPStatus.BAD_REQUEST,
                             reason=str(err))
        else:
            try:
                response = self.settings['mongo'].insert_one(new_user)
            except Exception as ex:
                logger.error(ex)
                raise ErrorThrow(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                 reason=str(ex))
            else:
                new_user = self.settings['mongo'].find_one(response)
                formatted_new_user = data_formatter.object_id_and_timestamp('created_at', new_user)
                self.write_response(status_code=HTTPStatus.CREATED,
                                    result=formatted_new_user)

    def put(self, key):
        try:
            UserSchema().load(self.data_received())

        except ValidationError as err:
            logger.error(err)
            raise ErrorThrow(status_code=HTTPStatus.BAD_REQUEST,
                             reason=str(err))
        else:
            try:
                response = self.settings['mongo'].update_one(key, self.data_received())

                formatted_response = data_formatter.object_id_and_timestamp('created_at', response)
            except ValueError:
                raise ErrorThrow(status_code=HTTPStatus.BAD_REQUEST,
                                 reason='no user found with id {}'.format(key))
            except Exception as ex:
                logger.error(ex)
                raise ErrorThrow(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                 reason=str(ex))
            else:
                self.write_response(status_code=HTTPStatus.OK,
                                    result=formatted_response)

    def delete(self, key):
        try:
            self.settings['mongo'].delete_one(key)
        except ValueError:
            raise ErrorThrow(status_code=HTTPStatus.BAD_REQUEST,
                             reason='no user found with id {}'.format(key))
        except Exception as ex:
            logger.error(ex)
            raise ErrorThrow(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                             reason=str(ex))
        else:
            self.write_response(status_code=HTTPStatus.OK,
                                message='the user was successfully deleted')
