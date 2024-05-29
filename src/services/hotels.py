from src.schemas.hotels import AddHotelSchema, HotelSchema
from src.utils.repository import AbstractRepository


class HotelsService:

    def __init__(self, hotel_repo: AbstractRepository):
        self.hotel_repo = hotel_repo()

    async def get_hotels(self):
        hotels = await self.hotel_repo.find_all()
        return hotels

    async def add_hotel(self, data: AddHotelSchema):
        return await self.hotel_repo.add_one(name=data.name, description=data.description, city=data.city)

    async def get_hotel_by_id(self, hotel_id):
        return await self.hotel_repo.find_by_id(hotel_id)

    async def delete_hotel_by_id(self, hotel_id):
        return await self.hotel_repo.delete_by_id(hotel_id)
