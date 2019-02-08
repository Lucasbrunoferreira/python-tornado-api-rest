from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):
    def set_default_headers(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header("Content-Type", "application/json")

    def write_error(self, status_code, **kwargs):
        self.finish(json.dumps({
            'error': {
                'code': status_code,
                'message': self._reason
            }
        }))

    def write_response(self, status_code, result):
        self.set_status(status_code)
        self.finish(json.dumps({
            'status_code': self.get_status(),
            'data': result
        }))
