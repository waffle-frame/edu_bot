from aiogram.types import Message
from telethon.client import TelegramClient
from sqlalchemy.orm import scoped_session

from models.groups import Group
from utils.userbot.group.create import create_megagroup


async def complex_action(message: Message, userbot: TelegramClient, 
                        db: scoped_session, data: dict) -> str:
    get_userbot = await userbot.get_me()
    userbot_data = f"{get_userbot.first_name} {get_userbot.last_name}"    

    group_id, link = await create_megagroup(userbot, data)

    insert = await Group.create(db,
        group_title = data["title"],
        occupation_type = data["occupation_type"],
        first_name = message['from'].first_name,
        last_name = message['from'].last_name,
        username = message['from'].username,
        user_id = message['from'].id,
        userbot = userbot_data,
        group_id = group_id - group_id * 2,
        link = link,
    )

    if not insert:
        return f"{link}\nВозникли некоторые трудности, свяжитесь с администратором!"

    return link
