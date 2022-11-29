from loguru import logger

from telethon.client import TelegramClient
from telethon.tl.types import ChatBannedRights, PeerChat 
from telethon.tl.functions.messages import CreateChatRequest, \
    EditChatAdminRequest, EditChatDefaultBannedRightsRequest

from utils.userbot.group.update_photo import update_photo
from utils.userbot.group.invite_link import generate_invite_link


async def create_group(client: TelegramClient, data: dict) -> str:
    """
        Create a private chat and set up.
        Add the user who used the command and grant admin rights.
    """

    try:
        result = await client(CreateChatRequest(
            users = [data["username"]], title = data["title"]
        ))
        chat_id = result.chats[0].id
    except Exception as e:
        result = await client(CreateChatRequest(
            users = ["educational_establishments_bot"], title = data["title"]
        ))
        chat_id = result.chats[0].id

        logger.error(e)
        logger.warning(f"Create new group! Data: {data})")
        await update_photo(client, chat_id, data['photo_path'])

        return await generate_invite_link(client, chat_id)

    # Grant admin rights
    await client(EditChatAdminRequest(
        chat_id = chat_id, user_id = data["user_id"], is_admin = True,
    ))

    # Configuring сhat access for users
    await client(EditChatDefaultBannedRightsRequest(
        peer = PeerChat(chat_id),
        banned_rights = ChatBannedRights(
            # Default
            until_date = None,
            view_messages = None,
            send_messages = None,
            # Allow
            send_polls = False,
            send_media = False,
            change_info = False,
            send_inline = False,
            pin_messages = False,
            # Deny
            send_gifs = True,
            send_games = True,
            invite_users = True,
            send_stickers = True,
        )
    ))

    return await generate_invite_link(client, chat_id)
