import asyncio
import functools


def make_sync(func):
    @functools.wraps(func)
    def inner(**kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(func(**kwargs))

    return inner
