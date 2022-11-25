# Packages
from loguru import logger as logrus
from aiogram.types.message import ParseMode
from aiogram import Bot, Dispatcher, executor

# Configs
from utils.config import load_config


conf = load_config()


# Setup dependencies, handlers, connections
async def start(dp: Dispatcher):
    import handlers
    from utils import logger

    logger.setup(conf.logger.path)
    logrus.info('Bot is successful running!')


# Stop bot and another connections
async def stop(dp: Dispatcher):
    pass


if __name__ == '__main__':
    bot = Bot(
        token = conf.bot.token,
        parse_mode = ParseMode.HTML,
        validate_token = True
    )
    dp = Dispatcher(bot)

    executor.start_polling(dp, on_startup = start, on_shutdown = stop, skip_updates = False)
