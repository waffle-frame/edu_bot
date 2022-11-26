from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class SQLAlchemyMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, db_factory: sessionmaker):
        super().__init__()
        self.db_factory = db_factory

    async def pre_process(self, obj, data, *args):
        db: AsyncSession = self.db_factory()
        data["database"] = db

    async def post_process(self, obj, data, *args):
        db: AsyncSession = data.get("database")
        await db.close()
