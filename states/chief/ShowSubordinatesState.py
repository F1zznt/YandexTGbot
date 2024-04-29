from aiogram.dispatcher.filters.state import StatesGroup, State


class ShowSubordinatesState(StatesGroup):
    Start = State()
    EditCod = State()
    Tools = State()