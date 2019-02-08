from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options

from logzero import logger
from settings import logger_config
from handlers.users import UsersHandler

define('port', default=8081)
define('version', default=1)


def make_app():
    endpoints = [
        ("/api/v%i/users" % options.version, UsersHandler)
    ]

    return Application(endpoints, debug=True)


if __name__ == '__main__':
    app = make_app()
    logger_config.set_default()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    logger.info('Listening server on port %i' % options.port)
    IOLoop.current().start()
