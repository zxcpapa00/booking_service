from src.schemas.users import UserRegisterSchema
from src.utils.auth import get_password_hash
from src.utils.repository import AbstractRepository
from fastapi.exceptions import HTTPException


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
