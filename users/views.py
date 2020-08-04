from fastapi import APIRouter, Depends, Request

from . import services
from .dantic import UserSignInRequest, UserSignInResponse, JWTLoginResponse

router = APIRouter()


async def get_request_user(request: Request):
    auth = request.headers.get('Authorization', '')
    if auth.startswith('Bearer '):
        token = auth[len('Bearer '):]
        import jwt
        import settings
        from users.models import User
        decoded_token = jwt.decode(token, settings.SECRET_KEY)
        user = await User.get(id=decoded_token['user_id'])
        return user
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


@router.get('/self', status_code=200)
async def get_user_self(user=Depends(get_request_user)):
    return UserSignInResponse.from_tortoise_orm(user)
