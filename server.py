from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from logzero import logger

from handlers.users import UsersHandler
from persistence.database import mongo, redisdb

import settings

define('version', default=1)


def make_app():
    endpoints = [
        (r'/api/v{}/users/?(.*)?'.format(options.version), UsersHandler)
    ]

    return Application(endpoints,
                       debug=True,
                       mongo=mongo.MongoDb(),
                       redis=redisdb.RedisDb())


if __name__ == '__main__':
    app = make_app()
    settings.config_logs()
    http_server = HTTPServer(app)
    http_server.listen(settings.APP_PORT)
    logger.info('Listening server on port {0}'.format(settings.APP_PORT))
    IOLoop.current().start()
