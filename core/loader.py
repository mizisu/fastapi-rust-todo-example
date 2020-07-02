import os
import importlib
from pathlib import Path
from typing import List

from fastapi import FastAPI, APIRouter
from tortoise.contrib.fastapi import register_tortoise


class Router:
    def __init__(self, module_name, router):
        self.module_name: str = module_name
        self.router: APIRouter = router


class Loader:

    def __init__(self, app: FastAPI, prefix_path=''):
        self.app = app
        self.prefix_path = prefix_path
        self.models: List[str] = []
        self.routers: List[Router] = []

    def load_apps(self, *modules: str):
        for module_name in modules:
            files = [Path(file).stem for file in os.listdir(module_name)]
            if 'models' in files:
                self.models.append(f"{module_name}.models")

            if 'views' in files:
                router = self._load_view_router(f"{module_name}.views")
                self.routers.append(Router(module_name, router))

        self._register_models()
        self._register_router()

    def _register_models(self):
        register_tortoise(
            self.app,
            db_url="sqlite://:memory:",
            modules={"models": self.models},
            generate_schemas=True,
            add_exception_handlers=True,
        )

    def _register_router(self):
        for router in self.routers:
            self.app.include_router(
                router.router,
                prefix=self.prefix_path,
                tags=[router.module_name.capitalize()],
            )

    @staticmethod
    def _load_view_router(view):
        view_module = importlib.import_module(view)
        router = getattr(view_module, 'router', None)
        if router is None:
            raise Exception(f"{view} dose not have router")
        else:
            return router
