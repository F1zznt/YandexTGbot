from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import exit_calldata


def create_panel(type, attribute='none', text='Назад'):
    panel = InlineKeyboardMarkup()
    panel.add(InlineKeyboardButton(text=text, callback_data=exit_calldata.new(type=type,
                                                                                 attribute=attribute)))
    return panel


inline_exit = create_panel