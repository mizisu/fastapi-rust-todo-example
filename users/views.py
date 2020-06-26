from typing import List

from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError

from .models import user, user_create, Users

router = APIRouter()


class Status(BaseModel):
    message: str


@router.get("/users", response_model=List[user])
async def get_users():
    return await user.from_queryset(Users.all())


@router.post("/users", response_model=user)
async def create_user(user: user_create):
    user_obj = await Users.create(**user.dict(exclude_unset=True))
    return await user.from_tortoise_orm(user_obj)


@router.get(
    "/user/{user_id}", response_model=user, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(user_id: int):
    return await user.from_queryset_single(Users.get(id=user_id))


@router.post(
    "/user/{user_id}",
    response_model=user,
    responses={
        404: {"model": HTTPNotFoundError}
    }
)
async def update_user(user_id: int, user: user_create):
    await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await user.from_queryset_single(Users.get(id=user_id))


@router.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await Users.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
