from os import environ
from aiogram.types import Message
from sqlalchemy.orm import scoped_session
from telethon.client import TelegramClient

from models.groups import Group
from utils.userbot.group.remove_user import remove_user_from_groups

async def remove_user(message: Message, db: scoped_session, userbot: TelegramClient):
    parse_command = message.get_full_command()
    if parse_command.__len__() != 2:
        return await message.answer("Неверный запрос")

    user_id = parse_command[1]
    if not user_id.isdigit():
        return await message.answer("Неверный запрос")

    if user_id == environ.get('userbot_id') or environ.get('bot_id') == user_id:
        return await message.answer("Неверный запрос")

    groups_list = await Group.get_user_groups_by_id(db, int(user_id))
    await remove_user_from_groups(userbot, int(user_id), groups_list)

    await message.answer("Успешно")
