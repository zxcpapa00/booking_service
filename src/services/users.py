from src.schemas.users import UserRegisterSchema, UserLoginSchema
from src.utils.auth import get_password_hash, verify_password, create_access_token
from src.utils.repository import AbstractRepository
from fastapi.exceptions import HTTPException
from fastapi import status, Response


class UsersService:

    def __init__(self, user_repo: AbstractRepository):
        self.user_repo = user_repo()

    async def register_user(self, user_data: UserRegisterSchema):
        existing_user = await self.user_repo.find_one_or_none(email=user_data.email)
        if existing_user:
            raise HTTPException(status_code=404)
        hashed_password = get_password_hash(user_data.password_hashed)
        user_id = await self.user_repo.add_one(username=user_data.username, email=user_data.email,
                                               password_hashed=hashed_password)
        return user_id

    async def auth_user(self, user_data: UserLoginSchema):
        user = await self.user_repo.find_one_or_none(email=user_data.email)
        if not user and not verify_password(user_data.password, user.password_hashed):
            return None
        return user

    async def login_user(self, response: Response, user_data: UserLoginSchema):
        user = await self.auth_user(user_data)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        access_token = create_access_token({"sub": str(user.id)})
        response.set_cookie("access_token", access_token, httponly=True)
        return access_token

    async def get_user(self, user_id):
        user = await self.user_repo.find_by_id(user_id)
        return user

    @staticmethod
    async def logout_user(response: Response):
        response.delete_cookie("access_token")
