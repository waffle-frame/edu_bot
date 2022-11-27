from datetime import datetime
import os
from loguru import logger
from telethon.tl.types import InputChatUploadedPhoto, ChatBannedRights, PeerChat 
from telethon.tl.functions.messages import CreateChatRequest, ExportChatInviteRequest, \
                                        EditChatPhotoRequest, EditChatAdminRequest, \
                                    EditChatDefaultBannedRightsRequest


# Create a private chat and set up
# Add the user who used the command and grant admin rights
async def create_group(client, data):
    # Create chat and add user
    result = await client(
        CreateChatRequest(users = [data["username"]], title = data["title"])
    )
    chat_id = result.chats[0].id

    # Grant admin rights
    await client(
        EditChatAdminRequest(chat_id = chat_id, user_id = data["user_id"], is_admin = True)
    )

    # Upload chat photo
    upload_file = await client.upload_file(file = data["image_path"])
    input_uploaded_photo = InputChatUploadedPhoto(upload_file)

    # Edit chat photo
    await client(
        EditChatPhotoRequest(chat_id = chat_id, photo = input_uploaded_photo)
    )

    # Delete temp photo after upload
    if os.path.exists(data["image_path"]):
        os.remove(data["image_path"])
    else:
        logger.error(f"File path {data['image_path']} not foud!")

    # Configuring сhat access for users
    result = await client(EditChatDefaultBannedRightsRequest(
        peer = PeerChat(chat_id),
        banned_rights = ChatBannedRights(
            # Default
            until_date = None,
            view_messages = None,
            send_messages = None,
            # Allow
            send_polls = False,
            send_media = False,
            change_info = False,
            send_inline = False,
            pin_messages = False,
            # Deny
            send_gifs = True,
            send_games = True,
            invite_users = True,
            send_stickers = True,
        )
    ))

    invite_link = await client(ExportChatInviteRequest(
        peer = PeerChat(chat_id),
        legacy_revoke_permanent = True,
        expire_date = datetime(2027, 6, 25),
        title = 'link',
    ))

    return invite_link.link
