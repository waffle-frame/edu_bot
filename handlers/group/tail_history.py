from aiogram.types import Message
from sqlalchemy.orm import scoped_session

from models.groups import Group
from keyboards.type_of_lesson import create_group_button_text


async def tail_history(message: Message, db: scoped_session):
    parse_command = message.get_full_command()

    if parse_command.__len__() == 2 and parse_command[1].isdigit():
        tail = await Group.select_history_tail(
            db, limit = int(parse_command[1])
        )
    else:
        tail = await Group.select_history_tail(db)

    tail_text = f'Последняя активность: ({tail.__len__()})\n\n'
    for i in tail:
        tail_text += f"{i[3].strftime('%m-%d-%y %H:%M')} {i[0]} ({i[2].value[:4]}.) <a href='{i[1]}'>Ссылка</a>\n"

    await message.answer(tail_text)
