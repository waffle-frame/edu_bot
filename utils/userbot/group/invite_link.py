from datetime import datetime, timedelta

from telethon.tl.types import PeerChat 
from telethon.client import TelegramClient
from telethon.tl.functions.messages import ExportChatInviteRequest


# Get invite link
async def generate_invite_link(client: TelegramClient, chat_id: int) -> str:
    invite = await client(ExportChatInviteRequest(
        peer = PeerChat(chat_id),
        expire_date = datetime.today() + timedelta(days=365),
        title = "link",
    ))

    return invite.link
