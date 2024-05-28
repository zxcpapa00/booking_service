import datetime
import uuid

from pydantic import BaseModel


class ReviewSchema(BaseModel):
    id: uuid.UUID
    comment: str
    star: int
    created_at: datetime.datetime
    user_id: uuid.UUID
    hotel_id: uuid.UUID
