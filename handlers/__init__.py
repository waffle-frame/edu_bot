from typing import Any

from aiogram import Dispatcher
from aiogram.types import ContentType
from aiogram.types import ContentType, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher.filters.builtin import Command

from states.create_group import CreateGroup
from handlers.base import register_base_commands
from handlers.create_group import pick_occupation_type, \
    set_group_title, get_group_image, question_for_set_image, set_group_image


def setup_handlers(dp: Dispatcher):
    print("enter!!!")
    register_base_commands(dp)

    dp.register_message_handler(pick_occupation_type, Command("create_group"), ChatTypeFilter(ChatType.PRIVATE), state="*")
    dp.register_message_handler(set_group_title, state=CreateGroup.occupation_type)
    dp.register_message_handler(question_for_set_image, state=CreateGroup.title)
    dp.register_message_handler(get_group_image, state=CreateGroup.image_question)
    dp.register_message_handler(set_group_image, content_types=ContentType.ANY, state=CreateGroup.image)
