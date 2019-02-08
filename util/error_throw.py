from tornado import web


class ErrorThrow(web.HTTPError):
    pass
