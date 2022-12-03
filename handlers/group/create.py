from aiogram.types import Message
from telethon.client import TelegramClient
from sqlalchemy.orm import scoped_session

from models.groups import Group
from utils.userbot.group.create import create_megagroup


async def complex_action(message: Message, userbot: TelegramClient, 
                        db: scoped_session, data: dict) -> str:
    get_userbot = await userbot.get_me()
    userbot_data = f"{get_userbot.first_name} {get_userbot.last_name}"    

    link = await create_megagroup(userbot, data)

    insert = await Group.create(db,
        group_title = data["title"],
        occupation_type = data["occupation_type"],
        first_name = message.chat.first_name,
        last_name = message.chat.last_name,
        username = message.chat.username,
        userbot = userbot_data,
        link = link,
    )

    if not insert:
        return "Упс... Что-то пошло не так"

    return link
