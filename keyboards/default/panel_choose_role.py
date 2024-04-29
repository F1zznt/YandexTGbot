from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_choose_role = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начальник'),
            KeyboardButton(text='Подчиненный'),
        ],
        [
            KeyboardButton(text='Назад'),
        ]
    ],
    resize_keyboard=True
)