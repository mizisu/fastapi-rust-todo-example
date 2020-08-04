from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import User


class UserSignInRequest(BaseModel):
    username: str
    password: str


UserSignInResponse = pydantic_model_creator(
    User,
    include=(
        'id',
    )
)


class JWTLoginResponse(BaseModel):
    access: str


UserSelfResponse = pydantic_model_creator(
    User,
    include=(
        'id',
        'username',
        'joined',
    )
)
