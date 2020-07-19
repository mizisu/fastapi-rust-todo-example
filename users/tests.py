import pytest
from core import status

from .models import User


def test_sign_in(client):
    response = client.post("api/v1/users/sign-in", json={
        "username": "admin",
        "password": "password",
    })
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    # await User.get(id=data["id"])
