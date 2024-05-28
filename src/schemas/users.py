import datetime
import uuid

from pydantic import BaseModel, EmailStr


class HotelSchema(BaseModel):
    id: uuid.UUID
    username: str
    password_hashed: str
    email: EmailStr
    role: str
    created_at: datetime.datetime
