from fastapi import APIRouter
from .models import Todo, todo

router = APIRouter()


@router.get("/todos", response_model=todo)
def get_todos():
    pass
