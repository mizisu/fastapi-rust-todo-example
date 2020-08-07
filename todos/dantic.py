from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Todo

TodoListResponse = pydantic_model_creator(
    Todo,
)