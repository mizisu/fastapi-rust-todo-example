import bcrypt

from .models import User


def create_user(username: str, password: str):
    user = await User.create(
        username=username,
        password=get_hash_password(password),
    )

    return user


def get_hash_password(password: str):
    return bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
