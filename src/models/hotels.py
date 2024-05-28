import uuid
from sqlalchemy import Column, String, Uuid, Text
from src.db.db import Base
from src.schemas.hotels import HotelSchema


class Hotels(Base):
    __tablename__ = 'hotels'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    city = Column(String, nullable=False)

    def to_read_model(self) -> HotelSchema:
        return HotelSchema(
            id=self.id,
            name=self.name,
            description=self.description,
            city=self.city
        )
