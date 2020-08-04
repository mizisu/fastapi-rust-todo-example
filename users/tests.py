from testing import *
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
        "username": user.username,
        "password": user.raw_password,
    })

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert 'access' in data


@make_sync
async def test_get_user_self(user_login_client):
    response = user_login_client.get("api/v1/users/self")
    assert response.status_code == status.HTTP_200_OK
