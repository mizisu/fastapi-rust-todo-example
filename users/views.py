from fastapi import APIRouter
from .models import User, UserSignInRes

router = APIRouter()


@router.post("/sign-in", status_code=201, response_model=UserSignInRes)
async def sign_in(username: str, password: str):
    user = await User.create(
        username=username,
        password=password,
    )
    return UserSignInRes.from_tortoise_orm(user)
