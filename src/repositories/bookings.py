from src.models.bookings import Bookings
from src.utils.repository import SQLAlchemyRepository


class BookingRepository(SQLAlchemyRepository):
    model = Bookings
