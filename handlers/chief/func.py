from aiogram.types import ReplyKeyboardRemove
from keyboards.default.chief import panel_subordinates_list, panel_tools_with_subordinate, \
    panel_task
from keyboards.inline.chief import inline_tools_show_subordinates
from loader import bot
from states.chief import ShowSubordinatesState, PanelTaskState


async def show_chief_panel(user_id):
    panel = panel_subordinates_list(user_id)
    n = len(panel.values["keyboard"])
    await bot.send_message(chat_id=user_id, text=f'Подчиненные: {n}',
                           reply_markup=panel if n != 0 else ReplyKeyboardRemove())
    await bot.send_message(chat_id=user_id, text='Инструменты',
                           reply_markup=inline_tools_show_subordinates)
    await ShowSubordinatesState.Start.set()


async def show_tools_with_subordinate(user_id):
    await bot.send_message(chat_id=user_id, text='Инструменты',
                           reply_markup=panel_tools_with_subordinate)
    await ShowSubordinatesState.Tools.set()


async def show_work_with_task_panel(user_id):
    await bot.send_message(chat_id=user_id,
                           text='Инструменты',
                           reply_markup=panel_task)
    await PanelTaskState.Start.set()
