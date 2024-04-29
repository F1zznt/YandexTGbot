from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_tools_with_task = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='В процессе'),
            KeyboardButton(text='Новые'),
        ],
        [
            KeyboardButton(text='Назад'),
        ],
    ],
    resize_keyboard=True
)