import uuid
from pydantic import BaseModel


class RoomSchema(BaseModel):
    id: uuid.UUID
    hotel_id: uuid.UUID
    type: str
    description: str
    price: int


class RoomsAddSchema(BaseModel):
    type: str
    description: str
    price: int
