from fastapi import APIRouter

from src.repositories.rooms import RoomRepository
from src.schemas.rooms import RoomSchema, RoomsAddSchema
from src.services.rooms import RoomsService

router = APIRouter(
    prefix="/hotels/{hotel_id}/rooms",
    tags=["Комнаты отелей"]
)


@router.get("")
async def get_rooms_hotel(hotel_id) -> list[RoomSchema]:
    hotels = await RoomsService(RoomRepository).get_rooms(hotel_id=hotel_id)
    return hotels


@router.post("")
async def add_rooms(hotel_id, data: RoomsAddSchema):
    return await RoomsService(RoomRepository).add_rooms(hotel_id, data)


@router.get("/{room_id}")
async def get_room_by_id(hotel_id, room_id):
    return await RoomsService(RoomRepository).get_room_by_id(hotel_id, room_id)


@router.delete("/{room_id}")
async def delete_room(hotel_id, room_id):
    return await RoomsService(RoomRepository).delete_rooms(room_id, hotel_id)
