from loguru import logger
from aiogram.types.message import ParseMode
from aiogram import Bot, Dispatcher, executor

from utils.config import load_config


conf = load_config()

# 
async def start(dp: Dispatcher):
    import handlers
    from utils import logrus

    logrus.setup(conf.logger.path)

    logger.info('Bot is successful running!')


# 
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
