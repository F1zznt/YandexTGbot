from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_save_add_file = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сохранить')
        ],
    ],
    resize_keyboard=True
)