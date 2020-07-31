import uvicorn
from fastapi import FastAPI

import settings
from core import Loader

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
