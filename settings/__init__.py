import os


def _load_env():
    import dotenv
    _env = dotenv.dotenv_values(".env")
    for k, v in _env.items():
        os.environ.setdefault(k, v)


_load_env()
BASE_DIR = os.path.abspath(
        os.path.dirname(
            os.path.dirname(__file__)
        )
)
SECRET_KEY = os.environ.get('SECRET_KEY')
JWT_ALGORITHMS = 'HS256'
ALLOW_ORIGINS = [
    'localhost'
]
