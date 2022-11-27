# Packages
from loguru import logger
from aiogram.types.message import ParseMode
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Configs
import handlers
from utils.config import load_config
from middlewares import setup_middlewares
from settings.logger import setup_logger
from settings.userbot import setup_userbot
from settings.database import setup_database

conf = load_config()


# Setup dependencies, handlers, connections
async def start(dp: Dispatcher):
    setup_logger(conf.logger.path)
    database = await setup_database(conf.database)
    client = await setup_userbot(conf.userbot)

    await setup_middlewares(dp, database, client)
    await handlers.setup_handlers(dp)

    logger.info('Bot is successful running!')


# Stop bot and another connections
async def stop(dp: Dispatcher):
    pass


if __name__ == '__main__':
    bot = Bot(
        token = conf.bot.token,
        parse_mode = ParseMode.HTML,
        validate_token = True
    )
    dp = Dispatcher(bot, storage=MemoryStorage())

    executor.start_polling(dp, on_startup = start, on_shutdown = stop, skip_updates = False)
