from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import task


def create_panel(task_id):
    panel = InlineKeyboardMarkup()
    panel.add(InlineKeyboardButton(text='Начать', callback_data=task.new(type='todo',
                                                                         attribute='start',
                                                                         info=str(task_id))))

    return panel


inline_new_task = create_panel
