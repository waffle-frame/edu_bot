from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateGroup(StatesGroup):
    occupation_type = State()
    title = State()
    image_question = State()
    image = State()
