from fastapi import APIRouter

from . import services
from .dantic import UserSignInReq, UserSignInRes, LoginJWTRes
from .models import User

router = APIRouter()


@router.post("/sign-in", status_code=201, response_model=UserSignInRes)
async def sign_in(body: UserSignInReq):
    new_user = await services.create_user(
        body.username,
        body.password,
    )
    return await UserSignInRes.from_tortoise_orm(new_user)


@router.post('/login', status_code=201, response_model=LoginJWTRes)
async def login(body: UserSignInReq):
    user = await services.login(
        body.username,
        body.password,
    )
