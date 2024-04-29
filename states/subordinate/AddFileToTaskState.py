from aiogram.dispatcher.filters.state import StatesGroup, State


class AddFileToTaskState(StatesGroup):
    AddVoice = State()
    AddPhoto = State()
    AddDocument = State()
