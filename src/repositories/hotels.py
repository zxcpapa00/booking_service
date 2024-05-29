from src.models.hotels import Hotels
from src.utils.repository import SQLAlchemyRepository


class HotelRepository(SQLAlchemyRepository):
    model = Hotels
