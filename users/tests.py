import asyncio
import pytest

from core import status

from .models import User


def test_sign_in(client, event_loop):
    response = client.post("api/v1/users/sign-in", json={
        "username": "admin",
        "password": "password",
    })
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data

    async def get_user_by_db():
        user = await User.get(id=data["id"])
        return user

    r = event_loop.run_until_complete(get_user_by_db())
    print("test")
    print(r)
