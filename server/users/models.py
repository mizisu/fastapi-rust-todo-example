from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    timestamp_created = fields.DatetimeField(auto_now_add=True)
    timestamp_updated = fields.DatetimeField(auto_now=True)
