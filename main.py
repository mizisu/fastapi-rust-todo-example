from fastapi import FastAPI

import loader
import users
import todos

app = FastAPI(title="TODO API")

loader.load_apps([
    "todos",
])

# app.include_router(users.router)
# app.include_router(
#     todos.router,
#     prefix='/api/v1',
#     tags=['Todos'],
# )
#
# register_tortoise(
#     app,
#     db_url="sqlite://:memory:",
#     modules={"models": ["users.models"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )
