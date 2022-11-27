from random import randint

from telethon.client import TelegramClient
from sqlalchemy.orm import scoped_session
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ContentType

from models.groups import Group
from states.create_group import CreateGroup
from utils.userbot.create_group import create_group
from keyboards.type_of_lesson import \
    type_of_lesson_kb, set_image_kb, get_create_group_button_text


async def pick_occupation_type(message: Message):
    await message.answer("Для отмены введите команду /cancel")
    await message.answer("Выберите тип занятий:", reply_markup = type_of_lesson_kb())
    await CreateGroup.occupation_type.set()


async def set_group_title(message: Message, state: FSMContext):
    if message.text not in get_create_group_button_text(0):
        return await message.answer("Вариант не существует")

    async with state.proxy() as data:
        data["occupation_type"] = message.text

    await message.answer("Введите название группы:", reply_markup = ReplyKeyboardRemove())
    await CreateGroup.title.set()


async def question_for_set_image(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["title"] = message.text

    await message.answer("Хотите установить фотографию?", reply_markup = set_image_kb())
    await CreateGroup.image_question.set()


async def get_group_image(message: Message, state: FSMContext):
    if message.text not in get_create_group_button_text(1):
        return await message.answer("Вариант не существует")

    if message.text == "Да":
        await message.answer("Отправьте фотографию <b>без сжатия</b>", reply_markup = ReplyKeyboardRemove())
        return await CreateGroup.image.set()

    await state.finish()


async def set_group_image(message: Message, state: FSMContext, db: scoped_session, userbot: TelegramClient):
    if message.content_type != ContentType.PHOTO:
        return await message.answer("Это не совсем похоже на фотографию.\nПопробуйте ещё раз")

    photo = message.photo[-1]
    if photo.width < 512 or photo.height < 512:
        return await message.answer("Эта фотография маленькая.\nМинимальный формат 512x512 пикселей")

    if message.chat.username == "":
        return await message.answer(
            "Ой..\nНе удалось создать чат. Ваш __username__ недоступен." +
            "\nПопробуйте установить в настройка, затем повторите поптыку"
        )

    path_to_image = f"tmp/temp-{randint(1, 100)}.png"

    await message.answer("Пожалуйста, подождите")
    await photo.download(destination_file = path_to_image)

    async with state.proxy() as data:
        data["image_path"] = path_to_image
        data["username"] = message.chat.username
        data["user_id"] = message.chat.id

    data = await state.get_data()
    get_userbot = await userbot.get_me()
    userbot_data = f"{get_userbot.first_name} {get_userbot.last_name}"    

    insert = await Group.create(db,
        group_title = data["title"],
        occupation_type = data["occupation_type"],
        first_name = message.chat.first_name,
        last_name = message.chat.last_name,
        username = message.chat.username,
        userbot = userbot_data,
    )

    await state.finish()
    if not insert:
        return await message.answer("Упс... Что-то пошло не так")

    invite_link = await create_group(userbot, data)
    await message.answer(f"Группа была успешно создана!\nПригласительная ссылка: {invite_link}")
