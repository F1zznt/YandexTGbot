from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_task = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить'),
        ],
        [
            KeyboardButton(text='Назад'),
            KeyboardButton(text='В главное меню'),
        ]
    ],
    resize_keyboard=True
)