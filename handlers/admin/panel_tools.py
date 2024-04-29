from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db import session
from db.data import Users, Tasks
from loader import dp
from states.admin import AdminState


@dp.message_handler(Text(equals=['Статистика']), state=AdminState.Start)
async def view_statistics(msg: Message):
    users = session.query(Users).all()
    tasks = session.query(Tasks).all()
    text = f'Пользователей: {len(users)}\n' \
           f'Задач: {len(tasks)}'
    await msg.answer(text=text)