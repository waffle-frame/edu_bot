from typing import List

from telethon.client import TelegramClient
from telethon.tl.types import PeerChannel, PeerUser 


async def remove_user_from_groups(client: TelegramClient, user_id: int,  groups: List[int]):
    """
        Exclude the user from the groups in which he is listed
    """

    for i in groups:
        all_participants = await client.get_participants(PeerChannel(i[0]))
        for j in all_participants:
            if j.id == user_id:
                await client.edit_permissions(
                    PeerChannel(i[0]), PeerUser(user_id), view_messages = False
                )

    return
