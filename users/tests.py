import pytest
from core import status

from .models import User


@pytest.mark.asyncio
async def test_sign_in(client):
    response = client.post("/users", json={
        "username": "admin",
        "password": "password",
    })
    assert response.status_code == status
    data = response.json()
    assert "id" in data
    await User.get(id=data["id"])
