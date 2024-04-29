from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_chief = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подчиненные'),
            KeyboardButton(text='Задачи'),
        ],
    ],
    resize_keyboard=True
)