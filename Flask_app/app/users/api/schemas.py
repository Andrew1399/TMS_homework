from dataclasses import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from marshmallow import fields

from app.models.base import User

class UserBaseSchema(SQLAlchemySchema):
    class Meta:
        model = User
    username = auto_field()

class UserCreateSchema(UserBaseSchema):
    password = fields.Str(required=True)

class UserReadSchema(UserBaseSchema):
    id = auto_field()