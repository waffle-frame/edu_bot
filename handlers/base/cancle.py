from loguru import logger
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove


# 
async def cancel_state(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logger.info(f'Cancelling state {current_state}')

    await state.reset_state()
    await message.reply('Диалог прекращён, данные удалены', reply_markup=ReplyKeyboardRemove())
