from fastapi import APIRouter

from src.repositories.users import UserRepository
from src.services.users import UsersService

from src.schemas.users import UserRegisterSchema

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: UserRegisterSchema):
    return await UsersService(UserRepository).register_user(user_data)
