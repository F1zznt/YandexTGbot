from aiogram.dispatcher.filters.state import StatesGroup, State


class AddTaskState(StatesGroup):
    Add = State()
    ChangeVoiceMessage = State()
    ChangeTitle = State()
