from typing import List

from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Todo

TodoListResponse = List[pydantic_model_creator(
    Todo,
    include=(
        'id',
        'content',
        'completed',
    )
)]
