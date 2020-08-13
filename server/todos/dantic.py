from typing import List

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Todo

TodoResponse = pydantic_model_creator(
    Todo,
    include=(
        'id',
        'content',
        'completed',
    )
)

TodoListResponse = List[TodoResponse]


class TodoCreateRequest(BaseModel):
    content: str


class TodoCreateResponse(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True
