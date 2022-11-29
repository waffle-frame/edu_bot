from loguru import logger
import os
from loguru import logger

from telethon.client import TelegramClient
from telethon.tl.types import InputChatUploadedPhoto 
from telethon.tl.functions.messages import EditChatPhotoRequest


async def update_photo(client: TelegramClient, chat_id: int, photo_path: str):
    """
        Upload and update group photo
    """

    if photo_path != "" and os.path.exists(photo_path):
        upload_file = await client.upload_file(file = photo_path)
        input_uploaded_photo = InputChatUploadedPhoto(upload_file)

        await client(EditChatPhotoRequest(
            chat_id = chat_id, photo = input_uploaded_photo
        ))

        if os.path.exists(photo_path):
            os.remove(photo_path)
        else:
            logger.error(f"File path {photo_path} not foud!")

    return
