from marshmallow import Schema, fields
import datetime as date


class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(
        missing=date.datetime.now(),
        default=date.datetime.now()
    )
