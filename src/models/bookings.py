import uuid
from sqlalchemy import Column, Uuid, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.db.db import Base


class Bookings(Base):
    __tablename__ = 'bookings'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(Uuid, ForeignKey('users.id', ondelete='CASCADE'))
    room_id = Column(Uuid, ForeignKey('rooms.id', ondelete='CASCADE'))

    user = relationship('Users', back_populates='bookings', cascade='all')
    room = relationship('Rooms', back_populates='booking', cascade='all')
