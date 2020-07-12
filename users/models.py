from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password_hash = fields.CharField(max_length=128, null=True)
    timestamp_created = fields.DatetimeField(auto_now_add=True)
    timestamp_modified = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ["password_hash"]


user = pydantic_model_creator(Users)
user_create = pydantic_model_creator(Users, exclude_readonly=True)
