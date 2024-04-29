from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import task

inline_add_task = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Отправить голосовое', callback_data=task.new(
                type='edit',
                attribute='voice_message',
                info='none'
            )),
            InlineKeyboardButton(text='Название', callback_data=task.new(
                type='edit',
                attribute='title',
                info='none'
            ))
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data=task.new(
                type='back',
                attribute='none',
                info='none'
            )),
            InlineKeyboardButton(text='Сохранить', callback_data=task.new(
                type='save',
                attribute='none',
                info='none'
            ))
        ]
    ]
)
