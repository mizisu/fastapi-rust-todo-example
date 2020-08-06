from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Todo

todo = pydantic_model_creator(Todo)
todo_create = pydantic_model_creator(
    Todo,
)