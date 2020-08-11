from fastapi import APIRouter, Depends, Request, HTTPException
from starlette import status

from . import services
from .dantic import UserSignInRequest, UserSignInResponse, JWTLoginResponse, UserSelfResponse

router = APIRouter()


async def get_request_user(request: Request):
    auth = request.headers.get('Authorization', '')
    user = None
    if auth.startswith('Bearer '):
        token = auth[len('Bearer '):]
        user = await services.get_user_from_token(token)

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    else:
        return user


@router.post("/sign-in", status_code=201, response_model=UserSignInResponse)
async def sign_in(body: UserSignInRequest):
    new_user = await services.create_user(
        body.username,
        body.password,
    )
    return await new_user


@router.post('/login', status_code=201, response_model=JWTLoginResponse)
async def login(body: UserSignInRequest):
    return await services.login(
        body.username,
        body.password,
    )


@router.get('/self', status_code=200, response_model=UserSelfResponse)
async def get_user_self(user=Depends(get_request_user)):
    return await user
