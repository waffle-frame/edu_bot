from telethon import TelegramClient

from utils.config import Userbot


# Authorization and session file generation
async def setup_userbot(conf: Userbot) -> TelegramClient:
    client = TelegramClient(
        "session", conf.api_id, conf.api_hash
    )
    await client.connect()

    return client
