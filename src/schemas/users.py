import datetime
import uuid

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: uuid.UUID
    username: str
    password_hashed: str
    email: EmailStr
    role: str
    created_at: datetime.datetime


class UserRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password_hashed: str


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserProfileSchema(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    role: str
    created_at: datetime.datetime
