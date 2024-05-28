import datetime
import uuid

from pydantic import BaseModel


class BookingSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    room_id: uuid.UUID
    start_date: datetime.datetime
    end_date: datetime.datetime
