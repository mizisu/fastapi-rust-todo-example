from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Todo(models.Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    timestamp_created = fields.DatetimeField(auto_now_add=True)
    timestamp_updated = fields.DatetimeField(auto_now=True)


todo = pydantic_model_creator(Todo)
todo_create = pydantic_model_creator(
    Todo,
)
