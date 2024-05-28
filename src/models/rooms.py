import uuid
from sqlalchemy import Column, String, Uuid, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.db.db import Base
from src.schemas.rooms import RoomSchema


class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String(150), nullable=False)
    description = Column(Text)
    price = Column(Integer)
    hotel_id = Column(Uuid, ForeignKey('hotels.id', ondelete='CASCADE'))

    hotel = relationship('Hotels', back_populates='rooms', cascade='all')

    def to_read_model(self) -> RoomSchema:
        return RoomSchema(
            id=self.id,
            type=self.type,
            description=self.description,
            price=self.price,
            hotel_id=self.hotel_id
        )
