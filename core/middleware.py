from fastapi import Request


async def authenticate(request: Request, call_next):
    response = await call_next(request)
    return response
