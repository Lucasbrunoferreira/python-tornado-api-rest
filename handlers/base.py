from http import HTTPStatus
from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):
    def set_default_headers(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Content-Type", "application/json")

    def write_error(self, status_code, **kwargs):
        self.finish(json.dumps({
            'error': {
                'code': status_code,
                'message': self._reason
            }
        }))

    def write_response(self, status_code, result=None, message=None):
        self.set_status(status_code)
        if result:
            self.finish(json.dumps(result))
        elif message:
            self.finish(json.dumps({
                "message": message
            }))
        elif status_code:
            self.set_status(status_code)
            self.finish()
