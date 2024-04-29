from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from db import session
from db.data import Users


def create_panel(chief_id):
    panel = ReplyKeyboardMarkup(resize_keyboard=True)
    subordinates = session.query(Users).get(chief_id).subordinates
    for people in subordinates:
        panel.add(KeyboardButton(text=f'Имя: {people.name}(@{people.user_name})\n'
                                      f'id: {people.user_id}'))
    return panel


panel_subordinates_list = create_panel