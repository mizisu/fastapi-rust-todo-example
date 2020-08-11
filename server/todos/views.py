from fastapi import APIRouter

from .dantic import TodoListResponse, TodoCreateRequest, TodoCreateResponse
from .models import Todo

router = APIRouter()


@router.get('/', response_model=TodoListResponse)
async def get_todos():
    return await Todo.all()


@router.post('/', status_code=201, response_model=TodoCreateResponse)
async def create_todo(body: TodoCreateRequest):
    todo = await Todo.create(
        content=body.content
    )
    return todo
