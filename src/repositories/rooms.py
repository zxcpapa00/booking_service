from src.models.rooms import Rooms
from src.utils.repository import SQLAlchemyRepository


class RoomRepository(SQLAlchemyRepository):
    model = Rooms
