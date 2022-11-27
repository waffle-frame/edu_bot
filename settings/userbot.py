from telethon import TelegramClient

from utils.config import Userbot


# Authorization and session file generation
async def setup_userbot(conf: Userbot):
    client = TelegramClient(
        f'session_{conf.phone_number}', conf.api_id, conf.api_hash
    )

    return client
