from fastapi import APIRouter, Response, Depends

from src.models.users import Users
from src.repositories.users import UserRepository
from src.services.users import UsersService

from src.schemas.users import UserRegisterSchema, UserLoginSchema, UserProfileSchema
from src.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: UserRegisterSchema):
    return await UsersService(UserRepository).register_user(user_data)


@router.post("/login")
async def login_user(response: Response, user_data: UserLoginSchema):
    return await UsersService(UserRepository).login_user(response, user_data)


@router.post("/logout")
async def logout(response: Response):
    await UsersService(UserRepository).logout_user(response)


@router.get("/profile")
async def get_profile(user=Depends(get_current_user)) -> UserProfileSchema:
    return user
