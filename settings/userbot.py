from telethon import TelegramClient

from utils.config import Userbot


# Authorization and session file generation
async def setup_userbot(conf: Userbot):
    client = await TelegramClient(
        f'session_{conf.userbot.phone_number}', conf.userbot.api_id, conf.userbot.api_hash
    )

    await client.start(conf.userbot.phone_number)
    return client
