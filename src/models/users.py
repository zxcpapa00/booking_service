import uuid
from datetime import datetime

from sqlalchemy import Column, String, Uuid, DateTime
from sqlalchemy.orm import relationship

from src.db.db import Base
from src.schemas.users import UserSchema


class Users(Base):
    __tablename__ = 'users'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(150), unique=True, nullable=False)
    password_hashed = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    role = Column(String(5), default="user")
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    bookings = relationship('Bookings', back_populates='user', cascade='all')

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            username=self.username,
            password_hashed=self.password_hashed,
            email=self.email,
            role=self.role,
            created_at=self.created_at
        )
