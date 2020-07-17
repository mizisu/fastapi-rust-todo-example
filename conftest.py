from typing import Generator

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from main import app


@pytest.fixture(scope="module")
def client():
    initializer(["users.models"])
    with TestClient(app) as c:
        yield c
    finalizer()
