from fastapi import APIRouter

from .dantic import TodoListResponse
from .models import Todo

router = APIRouter()


@router.get("/", response_model=TodoListResponse)
async def get_todos():
    return await Todo.all()
