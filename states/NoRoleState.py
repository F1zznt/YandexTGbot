from aiogram.dispatcher.filters.state import StatesGroup, State


class NoRoleState(StatesGroup):
    Start = State()