from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import HTTPException
from starlette import status
from tortoise.exceptions import DoesNotExist

import settings

from .models import User


async def create_user(username: str, password: str) -> User:
    user = await User.create(
        username=username,
        password=get_hash_password(password),
    )

    return user


def get_hash_password(password: str) -> str:
    hash_password = bcrypt.hashpw(
        password.encode('UTF-8'),
        bcrypt.gensalt()
    )
    return hash_password.decode('UTF-8')


def check_password(user: User, password: str) -> bool:
    return bcrypt.checkpw(
        password.encode('UTF-8'),
        user.password.encode('UTF-8')
    )


def get_token(user: User) -> dict:
    access_token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }, settings.SECRET_KEY, settings.JWT_ALGORITHMS)

    return {
        'access': access_token.decode('UTF-8')
    }


async def get_user_from_token(token):
    try:
        decoded_token = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHMS]
        )
        user = await User.get(id=decoded_token['user_id'])
    except DoesNotExist:
        return None
    return user


async def login(username: str, password: str) -> dict:
    user = await User.get(username=username)
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    if check_password(user, password):
        return get_token(user)
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
