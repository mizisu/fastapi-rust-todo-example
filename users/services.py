import bcrypt

from .models import User


async def create_user(username: str, password: str):
    user = await User.create(
        username=username,
        password=get_hash_password(password),
    )

    return user


def get_hash_password(password: str):
    return bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())


async def login(username: str, password: str):
    user = User.get_or_none(username=username)
    if user is None:
        raise 404

    return bcrypt.checkpw(password, user.password)