from fastapi import APIRouter

from .dantic import TodoListResponse
from .models import Todo

router = APIRouter()


@router.get("/todos", response_model=TodoListResponse)
async def get_todos():
    return await TodoListResponse.from_tortoise_orm(Todo.all())
