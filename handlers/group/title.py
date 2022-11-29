from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from states.create_group import CreateGroup
from keyboards.type_of_lesson import create_group_button_text


async def set_group_title(message: Message, state: FSMContext):
    if message.text not in create_group_button_text(0):
        return await message.answer("Вариант не существует")

    async with state.proxy() as data:
        data["occupation_type"] = message.text

    await message.answer("Введите название группы:", reply_markup = ReplyKeyboardRemove())
    await CreateGroup.title.set()
