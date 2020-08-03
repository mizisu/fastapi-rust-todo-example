from fastapi import APIRouter, Depends, Request

from . import services
from .dantic import UserSignInRequest, UserSignInResponse, JWTLoginResponse

router = APIRouter()


async def get_request_user(request: Request):
    auth = request.headers.get('Authorization', '')
    if auth.startswith('Bearer '):
        token = auth[len('Bearer '):]
    return None


@router.post("/sign-in", status_code=201, response_model=UserSignInResponse)
async def sign_in(body: UserSignInRequest):
    new_user = await services.create_user(
        body.username,
        body.password,
    )
    return await UserSignInResponse.from_tortoise_orm(new_user)


@router.post('/login', status_code=201, response_model=JWTLoginResponse)
async def login(body: UserSignInRequest):
    return await services.login(
        body.username,
        body.password,
    )


@router.get('/test', status_code=200)
async def asdf(user=Depends(get_request_user)):
    pass
