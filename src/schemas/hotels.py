import uuid

from pydantic import BaseModel


class HotelSchema(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    city: str


class AddHotelSchema(BaseModel):
    name: str
    description: str
    city: str
