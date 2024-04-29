from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import task


def create_panel(task_id):
    panel = InlineKeyboardMarkup()
    panel.add(InlineKeyboardButton(text='Голосовухи',
                                   callback_data=task.new(type='in_progress',
                                                          attribute='voices',
                                                          info=str(task_id))),
              InlineKeyboardButton(text='Прикрепить файлы',
                                   callback_data=task.new(type='in_progress',
                                                          attribute='add_file',
                                                          info=str(task_id))),
              )
    panel.add(InlineKeyboardButton(text='Отправить',
                                   callback_data=task.new(type='done',
                                                          attribute='none',
                                                          info=str(task_id))))
    return panel


inline_progress_task = create_panel
