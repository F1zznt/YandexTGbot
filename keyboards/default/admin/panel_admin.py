from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Статистика'),
            KeyboardButton(text='Назад'),
        ],
    ],
    resize_keyboard=True
)
