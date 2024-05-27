import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Uuid, DateTime

from src.db.db import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(150), unique=True, nullable=False)
    password_hashed = Column(String(50), nullable=False)
    email = Column(String(200), unique=True)
    role = Column(String(5), default="user")
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
