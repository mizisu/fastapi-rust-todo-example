from fastapi import APIRouter
from .models import User, UserSignInRes, UserSignInReq

router = APIRouter()


@router.post("/sign-in", status_code=201, response_model=UserSignInRes)
async def sign_in(body: UserSignInReq):
    user = await User.create(
        username=body.username,
        password=body.password,
    )
    return await UserSignInRes.from_tortoise_orm(user)
