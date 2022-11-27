from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from middlewares.dependencies import SQLAlchemyMiddleware


async def setup_middlewares(dp: Dispatcher, db_factory: sessionmaker, userbot):
    dp.middleware.setup(SQLAlchemyMiddleware(db_factory, userbot))
