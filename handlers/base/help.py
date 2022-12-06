from os import environ
from aiogram.types import Message

from utils.config import load_config


async def help(message: Message):
    conf = load_config()
    help_message = "Помощь:\n" + \
        "/start — Запустить бота\n" + \
        "/help — Вывести это сообщение\n" + \
        "/create_group — Запустить процесс создания группы"

    print(message)

    if message['from'].id in conf.admins.admin_ids:
        help_message += "\n/history кол-во записей — Вывести список последних действий" + \
            f"\n\nДля поиска введите имя бота, после ключевые слова\nНапример:\n@{environ['bot_username']} grit"

    await message.answer(help_message)
