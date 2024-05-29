from fastapi import APIRouter, Response

from src.repositories.users import UserRepository
from src.services.users import UsersService

from src.schemas.users import UserRegisterSchema, UserLoginSchema

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
