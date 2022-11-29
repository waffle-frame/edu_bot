from aiogram.types import Message

from states.create_group import CreateGroup
from keyboards.type_of_lesson import type_of_lesson_kb


async def select_occupation_type(message: Message):
    await message.answer("Для отмены введите команду /cancel")
    await message.answer("Выберите тип занятий:", reply_markup = type_of_lesson_kb())
    await CreateGroup.occupation_type.set()
