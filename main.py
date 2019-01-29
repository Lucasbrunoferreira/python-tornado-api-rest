from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options

from handlers.users import UsersHandler

define('port', default=3000)


def make_app():
    endpoints = [
        ("/api/users", UsersHandler)
    ]

    return Application(endpoints, debug=True)


if __name__ == '__main__':
    app = make_app()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening server on port %i' % options.port)
    IOLoop.current().start()
