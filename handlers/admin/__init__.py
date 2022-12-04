from aiogram import Dispatcher
from aiogram.dispatcher.filters.builtin import Command, IDFilter

from utils.config import load_config 
from handlers.admin.remove_user import remove_user
from handlers.admin.tail_history import tail_history


def register_admin_commands(dp: Dispatcher):
    admin_ids = load_config().admins.admin_ids

    dp.register_message_handler(tail_history, IDFilter(user_id=admin_ids), Command("history"), state="*")
    dp.register_message_handler(remove_user, IDFilter(user_id=admin_ids), Command("remove_user"), state="*")
