from datetime import datetime, timedelta

from telethon.tl.types import PeerChannel
from telethon.client import TelegramClient
from telethon.tl.functions.messages import ExportChatInviteRequest


# Get invite link
async def generate_invite_link(client: TelegramClient, megagroup_id: int) -> str:
    """
       TODO: 
    """
    try:
        invite = await client(ExportChatInviteRequest(
            peer = PeerChannel(megagroup_id),
            expire_date = datetime.today() + timedelta(days=365),
            title = "link",
        ))

        return invite.link
    except Exception as e:
        print(e, "invite")
