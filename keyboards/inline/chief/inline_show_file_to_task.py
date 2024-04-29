from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import session
from db.data import Tasks
from keyboards.inline.callback_data import task


def create_panel(task_id):
    panel = InlineKeyboardMarkup()
    task_obj = session.query(Tasks).get(task_id)
    voices = task_obj.voices
    photos = task_obj.photos
    documents = task_obj.documents
    if voices:
        panel.add(InlineKeyboardButton(text='Аудиосообщения',
                                       callback_data=task.new(
                                           type='task_file',
                                           attribute='voices',
                                           info=str(task_id)
                                       )))
    if photos:
        panel.add(InlineKeyboardButton(text='Фотографии',
                                       callback_data=task.new(
                                           type='task_file',
                                           attribute='photos',
                                           info=str(task_id)
                                       )))
    if documents:
        panel.add(InlineKeyboardButton(text='Документы',
                                       callback_data=task.new(
                                           type='task_file',
                                           attribute='documents',
                                           info=str(task_id)
                                       )))
    return panel
    # panel.add(InlineKeyboardButton(text='Подтвердить',
    #                                callback_data=task.new(
    #                                    type='chief_show_task',
    #                                    attribute='done',
    #                                    info=str(task_id)
    #                                )))


inline_show_file_to_task = create_panel
