from fastapi import HTTPException, status

from src.models.bookings import Bookings
from src.repositories.rooms import RoomRepository
from src.services.rooms import RoomsService
from src.utils.repository import SQLAlchemyRepository


class BookingRepository(SQLAlchemyRepository):
    model = Bookings

    async def add_booking(self, user_id, room_id, start_date, end_date):
        room = await RoomsService(RoomRepository).get_room(room_id)
        if not room:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        booking = await self.find_by_filters(room_id=room_id)
        if start_date > end_date:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        if booking:
            if (booking.end_date < start_date) or ((booking.start_date > end_date) and (booking.end_date < end_date)):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Номер на эту дату занят")
        else:
            return await self.add_one(user_id=user_id, room_id=room_id, start_date=start_date, end_date=end_date)
