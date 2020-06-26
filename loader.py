import os
import importlib
from pathlib import Path
from typing import List
from tortoise.contrib.fastapi import register_tortoise


def load_apps(apps: List[str]):
    models = []
    routers = []
    for app in apps:
        files = [Path(file).stem for file in os.listdir(app)]
        if 'models' in files:
            models.append(f"{app}.models")

        if 'views' in files:
            router = _load_view_router(f"{app}.views")
            routers.append(router)


def _load_view_router(view):
    view_module = importlib.import_module(view)
    router = getattr(view_module, 'router', None)
    if router is None:
        raise Exception(f"{view} dose not have router")
