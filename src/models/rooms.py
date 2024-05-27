import uuid
from sqlalchemy import Column, String, Uuid, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.db.db import Base


class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String(150), nullable=False)
    description = Column(Text)
    price = Column(Integer)
    menu_id = Column(Uuid, ForeignKey('hotels.id', ondelete='CASCADE'))

    hotel = relationship('Hotels', back_populates='rooms', cascade='all')
