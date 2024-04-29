from aiogram.dispatcher.filters.state import StatesGroup, State


class SubordinateRoleState(StatesGroup):
    Start = State()
    TaskTools = State()
    NewTask = State()
    ProgressTask = State()
    ChooseTypeAddFile = State()