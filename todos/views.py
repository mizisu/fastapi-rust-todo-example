from fastapi import APIRouter

from .dantic import TodoListResponse
from .models import Todo

router = APIRouter()


@router.get("/")
async def get_todos():
    return await TodoListResponse.from_queryset(Todo.all())
