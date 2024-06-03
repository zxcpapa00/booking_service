from src.utils.repository import AbstractRepository


class RoomsService:

    def __init__(self, room_repo: AbstractRepository):
        self.room_repo = room_repo()

    async def get_room(self, room_id):
        return await self.room_repo.find_one_or_none(id=room_id)

    async def get_rooms(self, hotel_id):
        rooms = await self.room_repo.find_by_filters(hotel_id=hotel_id)
        return rooms

    async def add_rooms(self, hotel_id, data):
        return await self.room_repo.add_one(hotel_id=hotel_id, type=data.type, description=data.description,
                                            price=data.price)

    async def get_room_by_id(self, hotel_id, room_id):
        return await self.room_repo.find_one_or_none(hotel_id=hotel_id, id=room_id)

    async def delete_rooms(self, hotel_id, room_id):
        return await self.room_repo.delete_by_id(room_id, hotel_id=hotel_id)
