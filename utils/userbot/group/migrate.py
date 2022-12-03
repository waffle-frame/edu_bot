from telethon.client import TelegramClient
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.messages import MigrateChatRequest
from telethon.types import ChatAdminRights, PeerUser, PeerChannel


async def migrate_to_megagroup(client: TelegramClient, group_id: int,
                                data: dict, set_admin: bool = True) -> int:
    channel = await client(MigrateChatRequest(
        chat_id = group_id,
    ))
    channel_id = channel.chats[0].id

    if not set_admin:
        return channel_id

    await client(EditAdminRequest(
        channel=PeerChannel(channel_id),
        admin_rights=ChatAdminRights(),

        rank='some string here',
        user_id=PeerUser(data["user_id"])
    ))

    return channel_id
