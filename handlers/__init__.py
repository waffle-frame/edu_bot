from aiogram import Dispatcher
from handlers.base import register_base_commands


async def setup_handlers(dp: Dispatcher):
    await register_base_commands(dp)
