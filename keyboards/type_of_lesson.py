from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_create_group_button_text(func):
    match func:
        case 0:
            return ["Индивидуальные", "Групповые"] 
        case 1:
            return ["Да", "Нет"]


def type_of_lesson_kb():
    return ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True,
        keyboard = [ 
            [KeyboardButton(i) for i in get_create_group_button_text(0)]
        ]
    )


def set_image_kb():
    return ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True,
        keyboard = [ 
            [KeyboardButton(i) for i in get_create_group_button_text(1)]
        ]
    )
