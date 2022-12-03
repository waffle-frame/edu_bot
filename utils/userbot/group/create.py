from loguru import logger

from telethon.client import TelegramClient
from telethon.tl.functions.messages import CreateChatRequest, \
                                        AddChatUserRequest

from utils.userbot.group.update_photo import update_photo
from utils.userbot.group.migrate import migrate_to_megagroup
from utils.userbot.group.invite_link import generate_invite_link


async def create_megagroup(client: TelegramClient, data: dict) -> str:
    """
        Create a private chat and set up.
        Add the user who used the command and grant admin rights.
    """

    print(data)

    result = await client(CreateChatRequest(
        users = ["educational_establishments_bot"], title = data["title"]
    ))
    group_id = result.chats[0].id

    try:
        await AddChatUserRequest(
            chat_id = group_id, user_id = data["user_id"], fwd_limit = 0
        )
        await update_photo(client, group_id, data['photo_path'])
        await migrate_to_megagroup(client, data, group_id)
        return await generate_invite_link(client, group_id)

    except Exception as e:
        logger.error(e)

    await update_photo(client, group_id, data['photo_path'])
    await migrate_to_megagroup(client, group_id, data, False)

    return await generate_invite_link(client, group_id)
