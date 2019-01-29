import json

from handlers.base import BaseHandler
from persistence.users import users


class UsersHandler(BaseHandler):
    def get(self):
        self.set_status(200)
        self.write(json.dumps(users))
