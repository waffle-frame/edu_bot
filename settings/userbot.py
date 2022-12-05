from os import environ
from telethon import TelegramClient

from utils.config import Userbot


# Authorization and session file generation
async def setup_userbot(conf: Userbot) -> TelegramClient:
    client = TelegramClient(
        "session", conf.api_id, conf.api_hash
    )
    await client.start(conf.phone_number)

    userbot_data = await client.get_me()
    environ["userbot_id"] = userbot_data.id.__str__()

    return client
