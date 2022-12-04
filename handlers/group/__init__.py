from aiogram import Dispatcher
from aiogram.types import ContentType, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher.filters.builtin import Command

from states.create_group import CreateGroup
from handlers.group.title import set_group_title
from handlers.group.occupation_type import select_occupation_type
from handlers.group.photo import question_for_set_photo, get_group_photo, set_group_photo


def register_group_create_commands(dp: Dispatcher):
    dp.register_message_handler(
        select_occupation_type, Command("create_group"), ChatTypeFilter(ChatType.PRIVATE),  state="*"
    )
    dp.register_message_handler(set_group_title, state=CreateGroup.occupation_type)
    dp.register_message_handler(question_for_set_photo, state=CreateGroup.title)
    dp.register_message_handler(get_group_photo, state=CreateGroup.image_question)
    dp.register_message_handler(set_group_photo, content_types=ContentType.ANY, state=CreateGroup.image)
