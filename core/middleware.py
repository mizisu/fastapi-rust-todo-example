import logging

from fastapi import Request

logger = logging.getLogger(__name__)


async def authenticate(request: Request, call_next):
    response = await call_next(request)
    return response
