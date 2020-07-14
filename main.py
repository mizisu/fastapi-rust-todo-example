import uvicorn
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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
