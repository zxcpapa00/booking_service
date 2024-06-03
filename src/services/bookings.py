from src.utils.repository import AbstractRepository


class BookingsService:

    def __init__(self, booking_repo: AbstractRepository):
        self.booking_repo = booking_repo()

    async def get_bookings(self, user_id):
        bookings = await self.booking_repo.find_by_filters(user_id=user_id)
        return bookings

    async def add_booking(self, **data):
        return await self.booking_repo.add_booking(**data)
