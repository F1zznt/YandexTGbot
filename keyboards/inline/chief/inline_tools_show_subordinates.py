from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import exit_calldata, tools

inline_tools_show_subordinates = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить подчиненного',
                                 callback_data=tools.new(
                                     role='chief',
                                     type='add_subordinate'
                                 )),
        ],
        [
            InlineKeyboardButton(text='Назад',
                                 callback_data=exit_calldata.new(
                                     type='panel',
                                     attribute='none'
                                 ))
        ]
    ]
)
