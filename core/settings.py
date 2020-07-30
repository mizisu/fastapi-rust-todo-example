import os

import dotenv

env = dotenv.dotenv_values(".env")

for k, v in env.items():
    os.environ.setdefault(k, v)

SECRET_KEY = os.environ.get('SECRET_KEY')
