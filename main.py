from fastapi import FastAPI

from core import Loader

app = FastAPI(title="TODO API")

loader = Loader(
    app,
    prefix_path='/api/v1',
)

loader.load_apps(
    "users",
    "todos",
)
