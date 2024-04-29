from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_subordinate = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Задачи'),
        ],
        [
            KeyboardButton(text='Узнать свой код'),
        ],
    ],
    resize_keyboard=True
)