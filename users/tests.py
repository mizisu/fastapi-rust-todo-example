from core import *

from .models import User


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


@make_sync
async def test_login(client, user):
    response = client.post("api/v1/users/login", json={
        "username": "admin",
        "password": "password",
    })

    print(response.status_code)
