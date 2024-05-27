import datetime
import uuid
from sqlalchemy import Column, Uuid, Text, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.db.db import Base


class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    comment = Column(Text, nullable=True)
    star = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Uuid, ForeignKey('users.id', ondelete='CASCADE'))
    hotel_id = Column(Uuid, ForeignKey('hotels.id', ondelete='CASCADE'))

    user = relationship('Users', back_populates='reviews', cascade='all')
    hotel = relationship('Hotels', back_populates='review', cascade='all')
