from random import randint

from telethon.client import TelegramClient
from sqlalchemy.orm import scoped_session
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ContentType

from states.create_group import CreateGroup
from handlers.group.create import complex_action
from keyboards.type_of_lesson import set_image_kb, create_group_button_text


async def question_for_set_photo(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT:
        return await message.answer("Это не совсем похоже на текст")

    async with state.proxy() as data:
        data["title"] = message.text

    await message.answer("Хотите установить фотографию?", reply_markup=set_image_kb())
    await CreateGroup.image_question.set()


async def get_group_photo(message: Message, state: FSMContext, 
                            db: scoped_session, userbot: TelegramClient):
    if message.text not in create_group_button_text(1):
        return await message.answer("Вариант не существует")

    if message.text == "Да":
        await message.answer(
            "Отправьте фотографию <b>без сжатия</b>", reply_markup = ReplyKeyboardRemove()
        )
        return await CreateGroup.image.set()

    async with state.proxy() as data:
        data["photo_path"] = ""
        data["user_id"] = message['from'].id
        data["username"] = message['from'].username

    data = await state.get_data()
    invite_link = await complex_action(message, userbot, db, data)

    await state.finish()
    await message.answer(f"Группа была успешно создана!\nПригласительная ссылка: {invite_link}")


async def set_group_photo(message: Message, state: FSMContext, 
                            db: scoped_session, userbot: TelegramClient):
    if message.content_type != ContentType.PHOTO:
        return await message.answer("Это не совсем похоже на фотографию.\nПопробуйте ещё раз")

    photo = message.photo[-1]
    if photo.width < 512 or photo.height < 512:
        return await message.answer(
            "Эта фотография маленькая.\nМинимальный формат 512x512 пикселей"
        )

    path_to_image = f"tmp/temp-{randint(1, 100)}.png"
    await photo.download(destination_file = path_to_image)

    if message.chat.username != "":
        username = message.chat.username
    else:
        username = ""

    async with state.proxy() as data:
        data["photo_path"] = path_to_image
        data["user_id"] = message['from'].id
        data["username"] = username

    data = await state.get_data()
    invite_link = await complex_action(message, userbot, db, data)

    await state.finish()
    await message.answer(f"Группа была успешно создана!\nПригласительная ссылка: {invite_link}")
