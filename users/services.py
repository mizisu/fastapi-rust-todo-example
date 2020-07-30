from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import HTTPException
from core import status, settings

from .models import User


async def create_user(username: str, password: str):
    user = await User.create(
        username=username,
        password=get_hash_password(password),
    )

    return user


def get_hash_password(password: str):
    return bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())


def get_token(user):
    return jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }, settings.SECRET_KEY)


async def login(username: str, password: str):
    user = await User.get(username=username)
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    if bcrypt.checkpw(password, user.password):
        return get_token(user)
    else:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
