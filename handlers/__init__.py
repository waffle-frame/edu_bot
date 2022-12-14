from aiogram import Dispatcher

from handlers.base import register_base_commands
from handlers.admin import register_admin_commands
from handlers.group import register_group_create_commands

def setup_handlers(dp: Dispatcher):
    register_base_commands(dp)
    register_admin_commands(dp)
    register_group_create_commands(dp)
