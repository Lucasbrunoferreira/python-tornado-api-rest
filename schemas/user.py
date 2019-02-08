from marshmallow import Schema, fields
import datetime as date


class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    creat_at = fields.DateTime(default=date.datetime.utcnow())
