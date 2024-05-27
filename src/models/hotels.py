import uuid
from sqlalchemy import Column, String, Uuid, Text
from src.db.db import Base


class Hotels(Base):
    __tablename__ = 'hotels'

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    city = Column(String, nullable=False)

