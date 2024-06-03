from fastapi import APIRouter, Depends

from src.models.users import Users
from src.repositories.bookings import BookingRepository
from src.services.bookings import BookingsService
from src.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingsService(BookingRepository).get_bookings(user.id)
