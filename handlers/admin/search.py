from sqlalchemy.orm import scoped_session

from random import randint
from aiogram.types import InlineQuery, InputTextMessageContent, \
                        InlineQueryResultArticle, ChosenInlineResult

from models.groups import Group


##############################################################
#                TODO: NEED TO OPTIMISATION                  #
##############################################################

async def inline_echo(query: InlineQuery, db: scoped_session):
    text = query.query or "Поиск"

    result = []
    data = await Group.search(db, text, 11)

    for i in data:
        if data[i] == []:
            continue

        for j in data[i]:
            result.append(InlineQueryResultArticle(
                id = f'{i}_{text}_{str(randint(-10000000, 10000000))}',
                title = i,
                description = f'{j[1]} {j[2]}',
                input_message_content=InputTextMessageContent(text, parse_mode="HTML"),
            ))

    await query.answer(result, cache_time=1, is_personal=True)


async def get_similar_movies(query: ChosenInlineResult, db: scoped_session):
    parse_data = query.result_id.split("_")
    data = await Group.search(db, parse_data[1], 100000)

    text = "Вот что удалось найти:\n"

    if parse_data[0] == 'Пользователь':
        for i in data["Пользователь"]:
            text += f'<code>{i[0]} {i[1]}</code> (Групп: {i[3]}) -> {i[2]}\n'
    else:
        temp_date = ''
        for i in data["Группа"]:
            temp_text = f"<a href='{i[3]}'>{i[0]}</a> {i[1]} {i[2]} -> {i[4]}\n"
            if temp_date == i[5]:
                text += temp_text
                continue
            temp_date = i[5]
            text += f"\n{i[5]}:\n{temp_text}"
    return await query.bot.send_message(query.from_user.id, text)
