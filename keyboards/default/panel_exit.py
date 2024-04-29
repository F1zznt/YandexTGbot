from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_exit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад'),
        ],
    ],
    resize_keyboard=True
)