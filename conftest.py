from asyncio import AbstractEventLoop

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from main import app


@pytest.fixture(autouse=True)
def nest():
    import nest_asyncio
    nest_asyncio.apply()


@pytest.fixture(scope="function")
def client():
    initializer(["users.models"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="function")
def event_loop(client: TestClient) -> AbstractEventLoop:
    yield client.task.get_loop()


@pytest.fixture(scope="function")
def user(event_loop):
    from users import services
    user = event_loop.run_until_complete(services.create_user(
        'test',
        '1234'
    ))
    user.raw_password = '1234'
    return user


@pytest.fixture(scope='function')
def user_login_client(user, client):
    from users import services
    token = services.get_token(user)
    client.headers['Authorization'] = f"Bearer {token['access']}"
    return client
