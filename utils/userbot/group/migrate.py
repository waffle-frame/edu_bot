from telethon.client import TelegramClient
from telethon.tl.functions.channels import EditAdminRequest, \
                                    TogglePreHistoryHiddenRequest
from telethon.tl.functions.messages import MigrateChatRequest
from telethon.types import ChatAdminRights, PeerUser, PeerChannel


async def migrate_to_megagroup(client: TelegramClient, group_id: int,
                                data: dict, set_admin: bool = True) -> int:
    """
        TODO:
    """
    try:
        channel = await client(MigrateChatRequest(
            chat_id = (group_id),
        ))
        channel_id = channel.chats[0].migrated_to.channel_id

        if not set_admin:
            return channel_id

        await client(EditAdminRequest(
            channel = PeerChannel(channel_id),
            admin_rights = ChatAdminRights(
                other = True,
                ban_users = True,
                manage_call = True,
                change_info = True,
                pin_messages = True,
                invite_users = True,
                manage_topics = True,
                post_messages = True,
                delete_messages = True,

                edit_messages = False,
                add_admins = False,
                anonymous = False
            ),

            rank = '',
            user_id = PeerUser(data["user_id"])
        ))

        await client(TogglePreHistoryHiddenRequest(
            channel = PeerChannel(channel_id),
            enabled = False
        ))

        return channel_id
    except Exception as e:
        print(e, "migrate")
