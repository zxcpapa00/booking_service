from fastapi import APIRouter

from src.repositories.hotels import HotelRepository
from src.schemas.hotels import AddHotelSchema
from src.services.hotels import HotelsService

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@router.get("")
async def get_hotels():
    hotels = await HotelsService(HotelRepository).get_hotels()
    return hotels


@router.post("")
async def add_hotels(data: AddHotelSchema):
    return await HotelsService(HotelRepository).add_hotel(data)


@router.get("/{hotel_id}")
async def get_hotel_by_id(hotel_id):
    return await HotelsService(HotelRepository).get_hotel_by_id(hotel_id)


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id):
    return await HotelsService(HotelRepository).delete_hotel_by_id(hotel_id)
