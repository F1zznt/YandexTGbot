from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_tools_with_subordinate = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Удалить подчиненного'),
        ],
        [
            KeyboardButton(text='Назад'),
            KeyboardButton(text='Задачи'),
        ],
    ],
    resize_keyboard=True
)