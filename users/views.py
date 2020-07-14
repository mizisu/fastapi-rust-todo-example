from typing import List

from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError

from .models import User

router = APIRouter()


@router.post("/users")
async def sign_in(username: str, password: str):
    user_obj = await User.create(
        username=username,
        password=password,
    )

    return {}
