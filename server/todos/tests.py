from testing import *
from .models import Todo


@make_sync
async def test_get_all_todos(client):
    todo = await Todo.create(
        content="adf",
    )

    response = client.get('/api/v1/todos/')
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    item = data[0]
    assert item['content'] == todo.content


@make_sync
async def test_create_todo(client):
    response = client.post('/api/v1/todos/', json={
        'content': 'test'
    })
    assert response.status_code == status.HTTP_201_CREATED
    todo = await Todo.first()
    data = response.json()
    assert todo.id == data['id']
    assert todo.content == data['content']
