from aiogram import Dispatcher
from aiogram.dispatcher.filters.builtin import Command, CommandHelp, \
                                            CommandStart, Text

from handlers.base.help import help
from handlers.base.id import get_id
from handlers.base.start import start
from handlers.base.cancle import cancel_state


async def register_base_commands(dp: Dispatcher):
    dp.register_message_handler(cancel_state, Command("cancle"), Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(start, CommandStart(), state="*")
    dp.register_message_handler(help, CommandHelp(), state="*")
    dp.register_message_handler(get_id, Command("id"), state="*")
