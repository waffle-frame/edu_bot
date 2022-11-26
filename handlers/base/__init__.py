from aiogram import Dispatcher
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandStart

from handlers.base.help import help
from handlers.base.start import start


async def register_base_commands(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart(), state='*')
    dp.register_message_handler(help, CommandHelp(), state='*')
