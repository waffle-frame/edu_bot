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
    try:
        result = await client(CreateChatRequest(
            users = ["educational_establishments_bot"], title = data["title"]
        ))
        group_id = result.chats[0].id

        try:
            await client(AddChatUserRequest(
                chat_id = group_id, user_id = data["username"], fwd_limit = 100
            ))
            await update_photo(client, group_id, data['photo_path'])
            megagroup_id = await migrate_to_megagroup(client, group_id, data, True)
            return await generate_invite_link(client, megagroup_id)

        except Exception as e:
            logger.error(e)

        await update_photo(client, group_id, data['photo_path'])
        megagroup_id = await migrate_to_megagroup(client, group_id, data, False)
        return await generate_invite_link(client, megagroup_id)
    except Exception as e:
        print(e, "create")
