from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import User


class UserSignInReq(BaseModel):
    username: str
    password: str


UserSignInRes = pydantic_model_creator(
    User,
    include=(
        'id',
    )
)
