from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseRoleState(StatesGroup):
    Start = State()
