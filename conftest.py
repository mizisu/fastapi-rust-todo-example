from asyncio import AbstractEventLoop

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from main import app


@pytest.fixture(scope="function")
def client():
    initializer(["users.models"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="function")
def event_loop(client: TestClient) -> AbstractEventLoop:
    yield client.task.get_loop()
