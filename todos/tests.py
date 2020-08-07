from testing import *


@make_sync
async def test_get_all_todos(client):
    response = client.get('api/v1/todos')
    assert response.status_code == status.HTTP_200_OK
