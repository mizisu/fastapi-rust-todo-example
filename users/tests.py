import asyncio
import functools

from core import status

from .models import User


def make_sync(func):
    @functools.wraps(func)
    def inner(**kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(func(**kwargs))

    return inner


@make_sync
async def test_sign_in(client):
    response = client.post("api/v1/users/sign-in", json={
        "username": "admin",
        "password": "password",
    })
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data

    user = await User.get(id=data["id"])
    assert user.id == data['id']
