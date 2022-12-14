from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class SQLAlchemyMiddleware(LifetimeControllerMiddleware):
    def __init__(self, db_factory: sessionmaker, userbot):
        self.userbot = userbot
        self.db_factory = db_factory
        super().__init__()

    async def pre_process(self, obj, data, *args):
        db: AsyncSession = self.db_factory()
        client = await self.userbot.start()
        data["db"] = db
        data["userbot"] = client

    async def post_process(self, obj, data, *args):
        db: AsyncSession = data.get("db")
        await db.close()
