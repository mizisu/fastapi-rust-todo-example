from fastapi import APIRouter

from . import services
from .dantic import UserSignInRequest, UserSignInResponse, JWTLoginResponse

router = APIRouter()


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
