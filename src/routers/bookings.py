from fastapi import APIRouter, Depends

from src.models.users import Users
from src.repositories.bookings import BookingRepository
from src.schemas.bookings import AddBookingSchema
from src.services.bookings import BookingsService
from src.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingsService(BookingRepository).get_bookings(user.id)


@router.post("")
async def add_booking(data: AddBookingSchema, user: Users = Depends(get_current_user)):
    return await BookingsService(BookingRepository).add_booking(user_id=user.id, room_id=data.room_id,
                                                                start_date=data.start_date, end_date=data.end_date)
