from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db import session
from db.data import Users
from handlers.chief.func import show_chief_panel, show_tools_with_subordinate, \
    show_work_with_task_panel
from loader import dp
from states.chief import ShowSubordinatesState
import re


@dp.message_handler(content_types=['text'], state=ShowSubordinatesState.Start)
async def work_with_sub(msg: types.Message, state: FSMContext):
    text = msg.text
    pattern = r'Имя: [\w\s]*\(@\w*\)[\w\s]*: (\d*)'
    text = re.findall(pattern, text)
    if not text:
        return
    user_id = text[0]
    # user = session.query(Users).get(user_id)
    await ShowSubordinatesState.Tools.set()
    data = {'subordinate_id': user_id}
    await state.update_data(data)
    await show_tools_with_subordinate(msg.from_user.id)


@dp.message_handler(Text(equals=['Задачи']), state=ShowSubordinatesState.Tools)
async def start_notice(msg: Message, state: FSMContext):
    await show_work_with_task_panel(msg.from_user.id)


@dp.message_handler(Text(equals=['Удалить подчиненного']), state=ShowSubordinatesState.Tools)
async def delete_sub(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data['subordinate_id']
    user = session.query(Users).get(user_id)
    user.chief_id = None
    session.commit()
    await msg.answer(text='Подчиненный удален')
    await show_chief_panel(msg.from_user.id)


@dp.message_handler(Text(equals=['Назад']), state=ShowSubordinatesState.Tools)
async def back_from_tools(msg: types.Message, state: FSMContext):
    await state.set_data({})
    await show_chief_panel(msg.from_user.id)
