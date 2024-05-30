import uuid
from abc import ABC, abstractmethod
from sqlalchemy import insert, select, delete
from src.db.db import async_session_maker


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_one_or_none(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, *args, **kwargs):
        raise NotImplementedError

    async def find_by_filters(self, *args, **kwargs):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, **data) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [i[0].to_read_model() for i in res.all()]
            return res

    async def find_one_or_none(self, **filters):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()

    async def find_by_id(self, model_id: uuid.UUID):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(id=model_id)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()

    async def delete_by_id(self, model_id: uuid.UUID, **kwargs):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(id=model_id, **kwargs)
            await session.execute(stmt)
            await session.commit()

    async def find_by_filters(self, **filters):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filters)
            res = await session.execute(stmt)
            res = [i[0].to_read_model() for i in res.all()]
            return res
