from fastapi import APIRouter

from .dantic import TodoListResponse, TodoCreateRequest, TodoCreateResponse, TodoResponse
from .models import Todo

router = APIRouter()


@router.post('/', status_code=201, response_model=TodoCreateResponse)
async def create_todo(body: TodoCreateRequest):
    todo = await Todo.create(
        content=body.content
    )
    return todo


@router.get('/', response_model=TodoListResponse)
async def get_todos():
    return await Todo.all()


@router.get('/{todo_id}', response_model=TodoResponse)
async def get_todo(todo_id: int):
    todo = await Todo.get_or_none(id=todo_id)
    return todo
